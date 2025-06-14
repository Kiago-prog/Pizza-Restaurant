# 🍕 Pizza Restaurant API

A RESTful API built with Flask for managing a pizza restaurant's menus, including restaurants, pizzas, and their associations. This project follows the MVC pattern and uses SQLAlchemy with Flask-Migrate for ORM and database migrations.

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pizza-api-challenge.git
cd pizza-api-challenge
```

2. Create Virtual Environment and Install Dependencies
```bash
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
```
3. Environment Setup
Export your Flask app:
```bash
export FLASK_APP=server/app.py
```

4. Initialize and Migrate the Database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Seed the Database
```bash
python server/seed.py
```

### ✅ Validation Rules
RestaurantPizza.price must be between 1 and 30.

Relationships must be valid (pizza_id and restaurant_id must exist).

### 🧪 Testing with Postman
Open Postman

Click Import → Upload challenge-1-pizzas.postman_collection.json

Test each route:

View restaurants

Create restaurant-pizza relationships

Delete restaurants

Validate error handling

### 📌 Notes
This API uses Flask-SQLAlchemy for models and Flask-Migrate for migrations.

Project follows MVC separation for maintainability and clarity.

Seed file server/seed.py contains sample data for development/testing.

### 🧑‍💻 Author
Kiago
