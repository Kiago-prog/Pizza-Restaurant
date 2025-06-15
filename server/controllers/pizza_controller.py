from flask import Blueprint, jsonify
from ..models.pizza import Pizza

pizza_bp = Blueprint('pizzas', __name__)

# GET /pizzas - returns a list of pizzas
@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    response = [{
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    } for pizza in pizzas]
    return jsonify(response), 200
