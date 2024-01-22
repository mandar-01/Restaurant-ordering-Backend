import json
from flask import jsonify

def getList():
    file = open('json_data/restaurants.json')
    data = json.load(file)
    return jsonify(data)