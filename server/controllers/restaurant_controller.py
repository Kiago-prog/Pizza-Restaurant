from flask import Blueprint, jsonify, request
from ..models.restaurant import Restaurant
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..app import db

restaurant_bp = Blueprint("restaurant_bp", __name__)

@restaurant_bp.route("/", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants]), 200

@restaurant_bp.route("/<int:id>", methods=["GET"])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant.to_dict(include_pizzas=True)), 200

@restaurant_bp.route("/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return "", 204
