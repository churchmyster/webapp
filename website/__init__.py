import json
from flask import Flask, request
from flask_restful import Api, Resource

items = {}


def app():
    app = Flask(__name__)
    api = Api(app)

    # Global items list to be held in memory
    items = []
    
    
    class Items(Resource):        

        def get(self):
            return items 

        def post(self):
            json_data = request.get_json()
            for item in json_data:
                items.append(item)
            
            return 201  #Created

        def delete(self):
            items.clear()
            return 204  #Deleted 

    # Add Items resource to API
    api.add_resource(Items, "/items") 

    return app