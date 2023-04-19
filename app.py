from flask import Flask, render_template, request, redirect, url_for
import models, seed

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cooking")
def cooking():
    return render_template('recipes.html', ingredients=models.ingredients, recipes=models.recipes, fridge_items=models.fridge_items)

@app.route("/add",  methods=["POST"])
def build_fridge():
    quant = int(request.form["quantity"])
    ingredient = request.form["ingredient"]
    if ingredient in list(item.ingredient for item in models.fridge_items):
        for i in range(len(models.fridge_items)):
            if models.fridge_items[i].ingredient == ingredient:
                models.fridge_items.pop(i)

    new_item = models.FridgeItem(ingredient, quant)
    models.fridge_items.append(new_item)
    return redirect(url_for('cooking'))

if __name__ == "__main__":
    seed.seed_data()
    app.run()