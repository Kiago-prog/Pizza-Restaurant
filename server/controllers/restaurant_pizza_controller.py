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
    
      # Validation: restaurant and pizza must exist
    restaurant = Restaurant.query.get(restaurant_id)
    pizza = Pizza.query.get(pizza_id)
    if not restaurant or not pizza:
        return jsonify({"errors": ["Invalid restaurant or pizza ID"]}), 400

    # Create and save the RestaurantPizza
    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()
    
     # Build success response
    response = {
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza_id,
        "restaurant_id": rp.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }
    return jsonify(response), 201

