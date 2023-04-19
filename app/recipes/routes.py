from flask import render_template
from app.recipes import bp
from app.models.ingredients import Ingredient

@bp.route('/')
def index():
    ingredients = Ingredient.query.all()
    return render_template('recipes/index.html', ingredients=ingredients)