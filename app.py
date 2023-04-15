from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/recipes")
def cooking():
    class Recipe:
        def __init__(self, name):
            self.name = name
            self.ingredients = {}

    def __str__(self):
        return self.name
        
    def parseIngredients(recipe, ingredients):
        ingredients_list = ingredients.split()
        ingredients_list = ingredients_list[::-1]
        while (len(ingredients_list) > 0):
            if ingredients_list[0][1].isnumeric():
                quant = ingredients_list.pop(0).strip('()')
                ingredient = ingredients_list.pop(0)
                while (len(ingredients_list) > 0 and not ingredients_list[0][1].isnumeric()):
                    if ingredients_list[0] == '(Any)':
                        ingredients_list.pop(0)
                    else:
                        ingredient = ingredients_list.pop(0) + ' ' + ingredient
            recipe.ingredients[ingredient] = quant

    page_to_scrape = requests.get('https://stardewvalleywiki.com/Cooking')
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    recipe_header = soup.find('h2', string='Recipes')
    recipes_html = recipe_header.findNext('table')
    headers_html = recipes_html.findAll('tr')[0].findAll('th')
    headers = []
    for header in headers_html:
        headers.append(header.text)

    recipes = []

    for row in recipes_html.find('tbody').children:
        if len(list(row)) > 1:
            data = row.findAll('td')
            if len(data) > 1:
                recipe = Recipe(data[headers.index('Name')].text.rstrip('\n'))
                recipes.append(recipe)
                parseIngredients(recipe, data[headers.index('Ingredients')].text)

    all_ingredients = []

    for recipe in recipes:
        for ingredient in recipe.ingredients.keys():
            if not ingredient in list(r.name for r in recipes) and not ingredient in all_ingredients:
                all_ingredients.append(ingredient)

    return render_template('recipes.html', ingredients=all_ingredients, recipes=recipes)