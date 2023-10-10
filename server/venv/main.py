from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Restaurant, RestaurantPizza, Pizza
from flask_cors import CORS  # Import CORS for cross-origin support

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to avoid warning

    db.init_app(app)
    migrate = Migrate(app, db)

    # Enable CORS for the entire app (you can adjust origins and other settings as needed)
    CORS(app)

    @app.route('/restaurants', methods=['GET'])
    def get_restaurants():
        restaurants_list = Restaurant.query.all()
        results = [
            {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            } for restaurant in restaurants_list]

        return jsonify(results)

    @app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
    def get_restaurant(restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            restaurant_data = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": [
                    {
                        "id": pizza.id,
                        "name": pizza.name,
                        "ingredients": pizza.ingredients
                    } for pizza in restaurant.pizzas
                ]
            }
            return jsonify(restaurant_data)
        else:
            return jsonify({"error": "Restaurant not found"}), 404

    @app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
    def delete_restaurant(restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            # Delete associated RestaurantPizza entries
            RestaurantPizza.query.filter_by(restaurant_id=restaurant_id).delete()
            # Delete the restaurant
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        else:
            return jsonify({"error": "Restaurant not found"}), 404

    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        pizzas_list = Pizza.query.all()
        results = [
            {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            } for pizza in pizzas_list]

        return jsonify(results)

    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        if 1 <= price <= 30:  # Add price validation
            restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
            db.session.add(restaurant_pizza)
            db.session.commit()

            pizza = Pizza.query.get(pizza_id)
            if pizza:
                return jsonify({
                    "id": pizza.id,
                    "name": pizza.name,
                    "ingredients": pizza.ingredients
                }), 201
            else:
                return jsonify({"error": "Pizza not found"}), 404
        else:
            return jsonify({"errors": ["Validation errors"]}), 400

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
