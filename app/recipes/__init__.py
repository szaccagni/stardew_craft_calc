from flask import Blueprint

bp = Blueprint('posts', __name__)


from app.recipes import routes