from flask import render_template
from app.main import bp
from app.models.recipes import Recipe, empty_fridge

@bp.route('/')
def index():
    empty_fridge()
    return render_template('index.html')