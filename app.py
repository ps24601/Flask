from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resource.user import UserRegister
from resource.item import Item, ItemList
from resource.store import Store, StoreList
from db import db

app = Flask(__name__)
# this is to tell where to look for db
# further instead of sqlite db, we ccn have postgres, oracle etc
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
# to turn off the flask SQLALchemy tracker, but not the SQLALchemy tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
# secret key
app.secret_key = "ppsin"
api = Api(app)

# decorator to tell to create the databse and table before
# first request is run
@app.before_first_request
def create_tables():
    db.create_all()


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
    db.init_app(app)
    app.run(port = 5000, debug = True)
