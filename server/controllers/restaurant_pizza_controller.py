from flask import Blueprint, request, jsonify
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant
from ..app import db

restaurant_pizza_bp = Blueprint("restaurant_pizza_bp", __name__)

@restaurant_pizza_bp.route("/", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = int(data.get("price"))
        pizza_id = data.get("pizza_id")
        restaurant_id = data.get("restaurant_id")
        if not (1 <= price <= 30):
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza or not restaurant:
            return jsonify({"errors": ["Invalid restaurant or pizza"]}), 400

        new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_rp)
        db.session.commit()

        return jsonify(new_rp.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
