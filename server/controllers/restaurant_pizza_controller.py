from flask import Blueprint, request, jsonify
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant
from ..app import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

# POST /restaurant_pizzas - create a new restaurant-pizza link
@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validation: all fields present
    if price is None or pizza_id is None or restaurant_id is None:
        return jsonify({"errors": ["Missing data"]}), 400

    # Validation: price between 1 and 30
    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
