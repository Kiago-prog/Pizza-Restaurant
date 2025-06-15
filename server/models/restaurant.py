from ..app import db
from sqlalchemy.orm import relationship

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = relationship("RestaurantPizza", back_populates="restaurant", cascade="all, delete")

    def to_dict(self, include_pizzas=False):
        data = {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
        if include_pizzas:
            data["pizzas"] = [rp.pizza.to_dict() for rp in self.restaurant_pizzas]
        return data