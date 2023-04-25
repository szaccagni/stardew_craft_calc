from flask import render_template
from app.recipes import bp
from app.models.ingredients import Ingredient
from app.models.recipes import Recipe

@bp.route('/')
def index():
    ingredients = Ingredient.query.all()
    recipes = Recipe.query.all()
    return render_template('recipes/index.html', ingredients=ingredients, recipes=recipes)