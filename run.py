from app import app
from  db import db
db.init_app(app)

# decorator to tell to create the databse and table before
# first request is run
@app.before_first_request
def create_tables():
    db.create_all()
