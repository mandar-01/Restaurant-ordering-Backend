import json
from flask import jsonify

def getDetails(restaurant_id):
    file = open('json_data/restaurants.json')
    data = json.load(file)
    for restaurant in data["restaurants"]:
        if restaurant["id"] == restaurant_id:
            return jsonify(restaurant)
        
    return jsonify({})