from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    # this doesnt has self so itbelongs to class itself and not object
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type= float,
                        required = True,
                        help = "This cannot be blank!")
    parser.add_argument('store_id',
                        type= int,
                        required = True,
                        help = "Every item needs Store id!")

    @jwt_required()
    def get(self, name):

        item = ItemModel.findItem(name)
        if item:
            return item.json()
        return {'message': 'Item Not Found'}, 404

    
    def post(self,name):
        if ItemModel.findItem(name):        
            return {'message': "item {} already exists".format(name)}, 400 # 400 is bad request
        data = Item.parser.parse_args()        
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.insert()
        except:
            return {'message':"An Internal error occured"}, 500 # internal server error code
        
        return item.json(), 201

    def delete(self,name):
        item = ItemModel.findItem(name)
        if item:
            item.deleteFromDb()
            return {'message':'Item deleted'}
        return {'message': 'item not found'}, 404

    def put(self,name):

        data = Item.parser.parse_args()

        item = ItemModel.findItem(name)
        if item is None:
            item = ItemModel(name,data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.insert()
    
                        
        return item.json()
    
    
class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
