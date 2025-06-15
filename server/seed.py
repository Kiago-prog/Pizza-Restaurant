from app import db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

# Drop and recreate tables (for clean seeding)
print("Clearing database...")
db.drop_all()
db.create_all()