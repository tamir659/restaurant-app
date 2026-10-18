from server import app
from db import db
from models.category import Category
from models.dish import Dish

with app.app_context():
    if Category.query.count() == 0:
        pizza = Category(name="Pizza", image="pizza.jpg")
        pasta = Category(name="Pasta", image="pasta.jpg")
        drinks = Category(name="Drinks", image="drinks.jpg")

        db.session.add_all([pizza, pasta, drinks])
        db.session.commit()

        db.session.add_all([
            Dish(
                name="Margherita Pizza",
                price=45,
                description="Classic pizza with tomato sauce and cheese",
                image="pizza.jpg",
                is_gluten_free="False",
                is_vegeterian="True",
                category_id=pizza.id
            ),
            Dish(
                name="Pasta Alfredo",
                price=52,
                description="Creamy pasta with parmesan",
                image="pasta.jpg",
                is_gluten_free="False",
                is_vegeterian="True",
                category_id=pasta.id
            ),
            Dish(
                name="Cola",
                price=12,
                description="Cold drink",
                image="cola.jpg",
                is_gluten_free="True",
                is_vegeterian="True",
                category_id=drinks.id
            )
        ])

        db.session.commit()
        print("Data added successfully")
    else:
        print("Data already exists")