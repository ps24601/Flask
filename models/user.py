from db import db


# to link the class Usermodel to db, we make reference to db.Model
class UserModel(db.Model):
# to reference to which table
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def findByUsername(cls,username):
        return cls.query.filter_by(username = username).first()

    def saveUserToDb(self):
        db.session.add(self)
        db.session.commit()    

        
    @classmethod
    def findById(cls,userid):
        return cls.query.filter_by(id = userid).first()
        