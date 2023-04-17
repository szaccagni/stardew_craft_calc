fridge_items = []
recipes = []
ingredients = []

class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = {}

    def __str__(self):
        return self.name
    
class FridgeItem:
    def __init__(self, ingredient, quantity):
        self.ingredient = ingredient
        self.quantity = quantity

    def __str__(self):
        return f'${self.ingredient} (${self.quantity})'