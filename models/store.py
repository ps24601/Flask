
from db import db

class StoreModel(db.Model):

    __tablename__ = 'store'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

    # if we dont call json lot fo times this is okay
    # but if we do too many call for items in store then
    # we can remove laxy = 'dynamic
    # and isntead use 

    # item.json() for item in self.items(),   without .all()

    items = db.relationship('ItemModel', lazy = 'dynamic')

    def __init__(self,name):
        self.name = name


    def json(self):
        return {'name':self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod    
    def findStore(cls, name):
        return cls.query.filter_by(name = name).first()   # select * from items where name = name Limit 1
        
    # we dont need separate update anymore
    def saveStoreToDb(self):
        db.session.add(self)
        db.session.commit()
        # session here is collection of objects

   
    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()

        