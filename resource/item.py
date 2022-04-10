from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
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
        # 1. this is one way to implement
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # return {'item': None}, 404
        # # 2. another way
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # return {'item': item},200 if item else 404

        item = ItemModel.findItem(name)
        if item:
            return item.json()
        return {'message': 'Item Not Found'}, 404
        # return {'resource': name}
    
    def post(self,name):
        # we can use Item.findItem(name) also insetad of self.findItem(name)
        if ItemModel.findItem(name):
            # return {'item':{'name':row[0], price}}
        # if the header is not set then we can get error, like data not sent in json type
        # to vercome we can say that force= True, but this will then  force the conversion everytime, rather
        # we can use the silent type
        
            return {'message': "item {} already exists".format(name)}, 400 # 400 is bad request
        data = Item.parser.parse_args()        
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.insert()
        except:
            return {'message':"An Internal error occured"}, 500 # internal server error code
        
        # response code for succesful post (created) is 201 not 200
        # 202 is for accepted, that is when creating takes time, we return that it is accepted but not yet created.
        return item.json(), 201

    def delete(self,name):
        item = ItemModel.findItem(name)
        if item:
            item.deleteFromDb()
    
        return {'message': 'item deleted'}

    def put(self,name):

        # we can include this code where requried or we can make it part of class itself.

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
