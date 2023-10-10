from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float



db = SQLAlchemy()

class Restaurant(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    pizzas = db.relationship('RestaurantPizza', backref='restaurant')

class Pizza(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    restaurants = db.relationship('RestaurantPizza', backref='pizza')

class RestaurantPizza(db.Model):
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    pizza_id = Column(Integer, db.ForeignKey('pizza.id'))
    restaurant_id = Column(Integer, db.ForeignKey('restaurant.id'))
