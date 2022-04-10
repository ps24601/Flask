from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.findStore(name)
        if store:
            return store.json()        
        return {'meassage': "Store not exist"}, 404


    def post(self,name):
        if StoreModel.findStore(name):
            return {'message': "Store {} already Exists".format(name)}, 400

        store = StoreModel(name)
        try:
            store.saveStoreToDb()
        except:
            return {'message': "ana error occured"}, 500
        
        return store.json(), 201

    def delete(self,name):
        store = StoreModel.findStore(name)
        if store:
            store.deleteFromDb()
        
        return {'message': "Store Deleted"}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
