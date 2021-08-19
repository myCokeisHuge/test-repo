from app import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()  # creates db and all tables needed if doesn't already exist
