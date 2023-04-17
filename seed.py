from bs4 import BeautifulSoup
import requests
import models

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

def get_recipes():
    for row in recipes_html.find('tbody').children:
        if len(list(row)) > 1:
            data = row.findAll('td')
            if len(data) > 1:
                recipe = models.Recipe(data[headers.index('Name')].text.rstrip('\n'))
                recipes.append(recipe)
                parseIngredients(recipe, data[headers.index('Ingredients')].text)

def get_ingredients():
    all_ingredients = []
    for recipe in recipes:
        for ingredient in recipe.ingredients.keys():
            if not ingredient in list(r.name for r in recipes) and not ingredient in all_ingredients:
                all_ingredients.append(ingredient)
    return all_ingredients

def seed_data():
    get_recipes()
    models.recipes = recipes
    models.ingredients = get_ingredients()