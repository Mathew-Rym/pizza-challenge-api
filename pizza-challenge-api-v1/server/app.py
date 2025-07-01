# App setup
from flask import Flask, make_response
from flask_migrate import Migrate
from models import *
from controllers import *



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Welcome to the Pizza shop :)</h1>'

@app.route('/pizzas')
def pizza_route():
    return pizzas()

@app.route('/restaurants')
def restaurant_route():
    return restaurants()

@app.route('/restaurants/<int:id>',methods=['GET','DELETE'])
def restaurants_by_id_route(id):
    return restaurants_by_id(id)

@app.route('/restaurant_pizzas',methods=['GET','POST'])
def restaurant_pizzas_route():
    return restaurant_pizzas()

if __name__ == '__main__':
    app.run(port=5555, debug=True)
