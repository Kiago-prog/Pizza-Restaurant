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

# Create Pizzas
print("Seeding pizzas...")
p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella")
p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Pepperoni, Cheese")
p3 = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Bell Peppers, Olives, Onions")

# Add to DB session
db.session.add_all([r1, r2, r3, p1, p2, p3])
db.session.commit()
