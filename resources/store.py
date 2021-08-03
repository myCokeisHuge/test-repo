from flask_restful import Resource, reqparse
from app_code.models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field is required')

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store no found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'A store with that name already exists'}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while saving to the DB.'}, 500

        return store.json(), 201

    def put(self, name):
        data = Store.parser.parse_args()
        store = StoreModel.find_by_name(name)

        # check for store, if exists update name
        if store:
            store.name = data['name']
        else:
            return{"Message": "A store with that name does not exist"}

        try:
            store.save_to_db()
            return store.json(), 201
        except:
            return {'message': 'An error occurred while saving to the DB.'}, 500


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted.'}


class StoreList(Resource):
    def get(self):
        stores = {'stores': [store.json() for store in StoreModel.query.all()]}

        # returns store info or None
        if stores:
            return stores, 200
        else:
            return {"message": "No stores available"}
