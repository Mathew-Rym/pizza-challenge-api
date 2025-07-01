from app import app
from models import db,Pizza,Restaurant,RestaurantPizza


with app.app_context():
    
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()
    
    r1 = Restaurant(name="Pizza Inn", address="Airport N Rd, Nairobi")
    r2 = Restaurant(name="Flame Grill", address="Fedha Road, Nairobi")
    r3 = Restaurant(name="Pizza Hut", address="Thermoteq Plaza, Mombasa Road, Nairobi")

    p1 = Pizza(name="Margherita", ingredients="Tomato sauce, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato sauce, Mozzarella, Pepperoni")
    p3 = Pizza(name="BBQ Chicken", ingredients="BBQ sauce, Mozzarella, Chicken, Red onions")
    p4 = Pizza(name="Hawaiian", ingredients="Tomato sauce, Mozzarella, Ham, Pineapple")
    p5 = Pizza(name="Veggie Supreme", ingredients="Tomato sauce, Mozzarella, Mushrooms, Peppers, Onions, Olives")
    p6 = Pizza(name="Meat Lovers", ingredients="Tomato sauce, Mozzarella, Pepperoni, Sausage, Bacon, Ham")
    p7 = Pizza(name="Four Cheese", ingredients="Tomato sauce, Mozzarella, Parmesan, Cheddar, Blue cheese")
    p8 = Pizza(name="Peri Peri Chicken", ingredients="Peri Peri sauce, Mozzarella, Spicy chicken, Peppers")
    p9 = Pizza(name="Seafood Delight", ingredients="Tomato sauce, Mozzarella, Prawns, Calamari, Herbs")
    p10 = Pizza(name="Mexican Fiesta", ingredients="Tomato sauce, Mozzarella, Spicy beef, Jalapenos, Onions")
    
    db.session.add_all([r1,r2,r3,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10])
    db.session.commit()
    
    rp1 = RestaurantPizza(price=1000, pizza_id=1, restaurant_id=1)
    rp2 = RestaurantPizza(price=1200, pizza_id=2, restaurant_id=1)
    rp3 = RestaurantPizza(price=1500, pizza_id=3, restaurant_id=1)
    rp4 = RestaurantPizza(price=1100, pizza_id=4, restaurant_id=1)

    rp5 = RestaurantPizza(price=1300, pizza_id=5, restaurant_id=2)
    rp6 = RestaurantPizza(price=1700, pizza_id=6, restaurant_id=2)
    rp7 = RestaurantPizza(price=1400, pizza_id=7, restaurant_id=2)
    rp8 = RestaurantPizza(price=1600, pizza_id=8, restaurant_id=2)

    rp9 = RestaurantPizza(price=1800, pizza_id=9, restaurant_id=3)
    rp10 = RestaurantPizza(price=1500, pizza_id=10, restaurant_id=3)


    db.session.add_all([rp1,rp2,rp3,rp4,rp5,rp6,rp7,rp8,rp9,rp10])
    db.session.commit()
    
    print("Seeded successfully :)")