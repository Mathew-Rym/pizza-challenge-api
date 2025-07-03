
from models import Pizza
from flask import make_response



def pizzas():
    pizzas = []
    for pizza in Pizza.query.all():
        pizza_dict ={
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        pizzas.append(pizza_dict)
    
    return make_response(
        pizzas,
        200
    )