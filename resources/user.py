import sqlite3
from flask_restful import Resource, reqparse
from app_code.models.user import UserModel


class UserRegister(Resource):
    # parse json payload
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field is required')
    parser.add_argument('password', type=str, required=True, help='This field is required')

    def post(self):
        data = UserRegister.parser.parse_args()  # assign parsed data to a variable

    # check if username already exists
        if UserModel.find_by_username(data['username']):
            return{"message:": "A user with that username already exists."}, 400

        # If doesn't exist, inserts a single user in DB
        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201
