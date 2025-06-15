from flask import Blueprint, jsonify, request
from ..models.restaurant import Restaurant
from ..models.restaurant_pizza import RestaurantPizza
from ..app import db

restaurant_bp = Blueprint('restaurants', __name__)

# GET /restaurants - list all restaurants
@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    response = [{
        "id": r.id,
        "name": r.name,
        "address": r.address
    } for r in restaurants]
    return jsonify(response), 200