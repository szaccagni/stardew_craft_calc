from app.extensions import db
import sqlite3

FRIDGE_ITEMS = {}

recipe_ingredient = db.Table('recipe_ingredient',
                             db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
                             db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')), 
                             db.Column('quantity', db.Integer))

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    ingredients = db.relationship('Ingredient', secondary=recipe_ingredient, backref='recipes')

    def __repr__(self):
        return f'<Recipe {self.name}>'

def empty_fridge():
    FRIDGE_ITEMS.clear()

def add_fridge_item(ingredient, quant):
    if ingredient in FRIDGE_ITEMS.keys():
        FRIDGE_ITEMS[ingredient] += int(quant)
    else:
        FRIDGE_ITEMS[ingredient] = int(quant)
    print(FRIDGE_ITEMS)


def execute_query(query):
    connection = sqlite3.connect('app.db')
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result
