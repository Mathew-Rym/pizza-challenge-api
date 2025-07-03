from . import db, SerializerMixin

class Pizza(db.Model,SerializerMixin):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.Text)
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')
    serialize_rules = ('-restaurant_pizzas.pizza',)

    
    def __repr__(self):
        return f'<Pizza {self.name}, {self.ingredients}>'