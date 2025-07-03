from app import db
from models import Restaurant
from flask import request,make_response



def restaurants():
    restaurants = []
    for restaurant in Restaurant.query.all():
        restaurant_dict = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
        restaurants.append(restaurant_dict)
    return make_response(
        restaurants,
        200
    )
    

def restaurants_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()
    if restaurant:
        if request.method == 'GET':
            return make_response(
                restaurant.to_dict(),
                200
            )
        elif request.method == 'DELETE':
            db.session.delete(restaurant)
            db.session.commit()
            
            response_body ={
                "deleted_successfully": True,
                "message": "Restaurant deleted successfully"
            }
            return make_response(
                response_body,
                200
            )
    else:
        response_body={
            "error":"Restaurant not found",
        }
        return make_response(
            response_body,
            404
        )