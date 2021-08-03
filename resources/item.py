import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from app_code.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field is required')
    parser.add_argument('store_id', type=int, required=True, help='This field is required')

    @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message': "An error occurred while searching for item."}, 500  # internal server error

        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        # check for item, if exists update price, else create it
        if item is None:
            item = ItemModel(name, **data)    # data['price'], data['store_id']...
        else:
            return {'message': "An item with that name already exists."}, 500  # internal server error

        # try to save to DB, on fail return error
        try:
            item.save_to_db()
        except:
            return {'message': "An error occurred inserting item."}, 500  # internal server error

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': "Item deleted"}, 200  # success

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        # check for item, if exists update price, else create it
        if item is None:
            item = ItemModel(name, **data)  # data['price'], data['store_id']...
        else:
            item.price = data['price']

        # save to db and return item info as json message
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        # items = {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        items = {'items': [item.json() for item in ItemModel.query.all()]}

        # returns item info or None
        if items:
            return items, 200
        else:
            return {"items": None}
