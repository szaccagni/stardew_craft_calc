from flask import render_template, request, redirect
from app.recipes import bp
from app.models.ingredients import Ingredient
from app.models.recipes import Recipe, recipe_ingredient, FRIDGE_ITEMS, add_fridge_item, execute_query

@bp.route('/')
def index():
    ingredients = Ingredient.query.all()
    recipes = Recipe.query.all()
    return render_template('recipes/index.html', ingredients=ingredients, recipes=recipes, fridge_items=FRIDGE_ITEMS)

@bp.route('/fridge', methods=['POST'])
def build_fridge():
    add_fridge_item(request.form.get("ingredient"), request.form.get("quant"))
    return redirect("/recipes")

@bp.route('/calc')
def calc():
    recipes = Recipe.query.all()
    r_i = execute_query('SELECT * FROM recipe_ingredient')
    print(r_i)
    return redirect("/recipes")