import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                         type = str,
                         required = True,
                         help = "Mandatory field")
    parser.add_argument('password',
                         type = str,
                         required = True,
                         help = "Mandatory field")                         
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.findByUsername(data['username']):
            return {"message": "User already exists"}, 400
        
        user = UserModel(**data)
        user.saveUserToDb()

        return {"message": "User created succesfully"}, 201

