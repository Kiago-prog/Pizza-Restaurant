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

# Create RestaurantPizzas
print("Linking pizzas to restaurants...")
rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
rp3 = RestaurantPizza(price=8, restaurant_id=r2.id, pizza_id=p1.id)
rp4 = RestaurantPizza(price=15, restaurant_id=r2.id, pizza_id=p3.id)
rp5 = RestaurantPizza(price=9, restaurant_id=r3.id, pizza_id=p2.id)

db.session.add_all([rp1, rp2, rp3, rp4, rp5])
db.session.commit()

print("🌱 Seeding complete!")