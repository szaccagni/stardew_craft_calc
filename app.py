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
    quant = request.form["quantity"]
    ingredient = request.form["ingredient"]
    new_item = models.FridgeItem(ingredient, quant)
    models.fridge_items.append(new_item)
    return redirect(url_for('cooking'))

if __name__ == "__main__":
    seed.seed_data()
    app.run()