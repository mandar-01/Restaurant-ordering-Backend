from flask import Flask, request
from .restaurant_list import getList
from.restaurant_details import getDetails
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getRestaurants',methods=['GET'])
def getRestaurantList():
    return getList()

@app.route('/getRestaurantDetails',methods=['GET'])
def getRestaurantDetails():
    return getDetails(request.args.get('restaurantId'))