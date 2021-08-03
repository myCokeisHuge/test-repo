# package imports
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


# user created file imports
from app_code.db import db
from app_code.security import authenticate, identity
from app_code.resources.user import UserRegister
from app_code.resources.item import Item, ItemList
from app_code.resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()  # creates db and all tables needed if doesn't already exist


jwt = JWT(app, authenticate, identity)  # /auth

# http://127.0.0.1:5000/item/<name>
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')  # 'UserRegister' class in user.py


if __name__ == '__main__':  # prevents app from executing if this file is imported into another
    db.init_app(app)
    app.run(port=5000, debug=False)
