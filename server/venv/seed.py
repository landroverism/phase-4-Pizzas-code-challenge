from models import db, Restaurant, Pizza, RestaurantPizza

def seed_db():
    db.create_all()

    # Add sample data
    pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')

    restaurant1 = Restaurant(name='Sottocasa NYC', address='298 Atlantic Ave, Brooklyn, NY 11201')
    restaurant2 = Restaurant(name='PizzArte', address='69 W 55th St, New York, NY 10019')

    # Add additional pizzas and restaurants to support new routes
    pizza3 = Pizza(name='Margherita', ingredients='Dough, Tomato Sauce, Basil, Mozzarella')
    pizza4 = Pizza(name='Hawaiian', ingredients='Dough, Tomato Sauce, Ham, Pineapple, Cheese')

    restaurant3 = Restaurant(name='Pizza Palace', address='123 Main St, Anytown, USA')
    restaurant4 = Restaurant(name='Pizza Haven', address='456 Elm St, Otherplace, USA')

    # Set up RestaurantPizza entries to associate pizzas with restaurants
    rp1 = RestaurantPizza(price=10.0, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
    rp2 = RestaurantPizza(price=15.0, pizza_id=pizza2.id, restaurant_id=restaurant2.id)
    rp3 = RestaurantPizza(price=12.0, pizza_id=pizza3.id, restaurant_id=restaurant3.id)
    rp4 = RestaurantPizza(price=14.0, pizza_id=pizza4.id, restaurant_id=restaurant4.id)

    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.add(pizza3)
    db.session.add(pizza4)
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(restaurant3)
    db.session.add(restaurant4)
    db.session.add(rp1)
    db.session.add(rp2)
    db.session.add(rp3)
    db.session.add(rp4)

    db.session.commit()

if __name__ == '__main__':
    seed_db()
