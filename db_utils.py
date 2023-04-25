from app.extensions import db
from app.models.ingredients import Ingredient
from app.models.recipes import Recipe, recipe_ingredient

INGREDIENTS = ['Egg', 'Milk', 'Vinegar', 'Dandelion', 'Leek', 'Cheese', 'Cauliflower', 'Wheat Flour', 'Bream', 'Sunfish', 'Parsnip', 'Beet', 'Tomato', 'Oil', 'Squid', 'Void Mayonnaise', 'Periwinkle', 'Blue Jazz', 'Sea Cucumber', 'Morel', 'Common Mushroom', 'Green Bean', 'Sugar', 'Yam', 'Carp', 'Potato', 'Kale', 'Amaranth', 'Salmon', 'Mayonnaise', 'Red Cabbage', 'Tuna', 'Largemouth Bass', 'Hot Pepper', 'Shrimp', 'Coconut', 'Green Algae', 'Rainbow Trout', 'Melon', 'Rhubarb', 'Eel', 'Any Fish', 'Rice', 'Seaweed', 'Corn', 'Radish', 'Eggplant', 'Blueberry', 'Pumpkin', 'Artichoke', 'Cranberries', 'Bok Choy', 'Hazelnut', 'Cave Carrot', 'Sardine', 'Winter Root', 'Coffee', 'Squid Ink', 'Midnight Carp', 'Flounder', 'White Algae', 'Wild Plum', 'Apricot', 'Blackberry', 'Apple', 'Garlic', 'Fiddlehead Fern', 'Poppy', 'Clam', 'Mussel', 'Crayfish', 'Snail', 'Lobster', 'Maple Syrup', 'Crab', 'Wild Horseradish', 'Ginger', 'Banana', 'Mango', 'Taro Root', 'Pineapple']

RECIPES = ['Fried Egg', 'Omelet', 'Salad', 'Cheese Cauliflower', 'Baked Fish', 'Parsnip Soup', 'Vegetable Medley', 'Complete Breakfast', 'Fried Calamari', 'Strange Bun', 'Lucky Lunch', 'Fried Mushroom', 'Pizza', 'Bean Hotpot', 'Glazed Yams', 'Carp Surprise', 'Hashbrowns', 'Pancakes', 'Salmon Dinner', 'Fish Taco', 'Crispy Bass', 'Pepper Poppers', 'Bread', 'Tom Kha Soup', 'Trout Soup', 'Chocolate Cake', 'Pink Cake', 'Rhubarb Pie', 'Cookie', 'Spaghetti', 'Fried Eel', 'Spicy Eel', 'Sashimi', 'Maki Roll', 'Tortilla', 'Red Plate', 'Eggplant Parmesan', 'Rice Pudding', 'Ice Cream', 'Blueberry Tart', 'Autumn\'s Bounty', 'Pumpkin Soup', 'Super Meal', 'Cranberry Sauce', 'Stuffing', 'Farmer\'s Lunch', 'Survival Burger', 'Dish O\' The Sea', 'Miner\'s Treat', 'Roots Platter', 'Triple Shot Espresso', 'Seafoam Pudding', 'Algae Soup', 'Pale Broth', 'Plum Pudding', 'Artichoke Dip', 'Stir Fry', 'Roasted Hazelnuts', 'Pumpkin Pie', 'Radish Salad', 'Fruit Salad', 'Blackberry Cobbler', 'Cranberry Candy', 'Bruschetta', 'Coleslaw', 'Fiddlehead Risotto', 'Poppyseed Muffin', 'Chowder', 'Fish Stew', 'Escargot', 'Lobster Bisque', 'Maple Bar', 'Crab Cakes', 'Shrimp Cocktail', 'Ginger Ale', 'Banana Pudding', 'Mango Sticky Rice', 'Poi', 'Tropical Curry', 'Squid Ink Ravioli']

def add_ingredients():
    for ingredient in INGREDIENTS:
        new_i = Ingredient(name=ingredient)
        db.session.add(new_i)
    db.session.commit()

def add_recipes():
    for recipe in RECIPES:
        new_r = Recipe(name=recipe)
        db.session.add(new_r)
    db.session.commit()