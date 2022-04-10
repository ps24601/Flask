
from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    store = db.relationship('StoreModel')

    def __init__(self,name,price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name, 'price': self.price}

    @classmethod    
    def findItem(cls, name):
        # use of SQLAlcehmy
        return cls.query.filter_by(name = name).first()   # select * from items where name = name Limit 1
        # conn = sqlite3.connect('data.db')
        # cursor = conn.cursor()

        # query = "SELECT * FROM items WHERE name = ?"
        # result = cursor.execute(query,(name,))
        # row = result.fetchone()
        # conn.close()

        # if row:
        #     return cls(row[0], row[1])
        #     # or cls(*row)

    # we dont need separate update anymore
    def insert(self):
        db.session.add(self)
        db.session.commit()
        # session here is collection of objects

   
    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()

        