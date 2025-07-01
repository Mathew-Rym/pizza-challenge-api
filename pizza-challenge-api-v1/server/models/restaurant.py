from . import db,SerializerMixin

class Restaurant(db.Model,SerializerMixin):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')
    serialize_rules = ('-restaurant_pizzas.restaurant',)
    
    def __repr__(self):
        return f'<Restaurant {self.name}, {self.address}>'