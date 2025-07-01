from app import db
from models import RestaurantPizza 
from flask import request, make_response


def restaurant_pizzas():
    if request.method == 'GET':
        restaurant_pizzas = [rp.to_dict() for rp in RestaurantPizza.query.all()]
        return make_response(
            restaurant_pizzas,
            200
        )
    
    elif request.method == 'POST':
        data = request.json
        new_restaurant_pizza = RestaurantPizza(
            price = data['price'],
            restaurant_id = data['restaurant_id'],
            pizza_id = data['pizza_id']
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        
        
        
        return make_response(
            new_restaurant_pizza.to_dict(),
            201
        )