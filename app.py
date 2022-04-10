from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resource.user import UserRegister
from resource.item import Item, ItemList
from resource.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
app.config['PROPOGATE_EXCEPTIONS'] = True
app.secret_key = "ppsin"
api = Api(app)

jwt = JWT(app, authenticate, identity)   # JWT creates new endpoint  which is /auth
 

api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister, '/register')

# debug lets you see the html of code where things might have gone wrong

if __name__ == '__main__':
# when python runs file it assigns name, when we runf ile directly it assign it name = __main__, 
# but not when referenced.
    from db import db
    db.init_app(app)
    app.run(port = 5000, debug = True)
