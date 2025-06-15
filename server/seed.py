from app import db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

# Drop and recreate tables (for clean seeding)
print("Clearing database...")
db.drop_all()
db.create_all()

# Create Restaurants
print("Seeding restaurants...")
r1 = Restaurant(name="Mama's Kitchen", address="123 Main St")
r2 = Restaurant(name="Kiki's Pizza", address="456 Side Ave")
r3 = Restaurant(name="Tony's Pizza Palace", address="789 Slice Blvd")
