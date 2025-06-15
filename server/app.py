### server/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .controllers.restaurant_controller import restaurant_bp
    from .controllers.pizza_controller import pizza_bp
    from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp, url_prefix="/restaurants")
    app.register_blueprint(pizza_bp, url_prefix="/pizzas")
    app.register_blueprint(restaurant_pizza_bp, url_prefix="/restaurant_pizzas")

    @app.route("/")
    def index():
        return {"message": "Welcome to the Pizza Restaurant API"}

    return app