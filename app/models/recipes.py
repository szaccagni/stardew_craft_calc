from app.extensions import db

recipe_ingredient = db.Table('recipe_ingredient',
                             db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
                             db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')), 
                             db.Column('quantity', db.Integer))

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    ingredients = db.relationship('Ingredient', secondary=recipe_ingredient, backref='recipes')

    def __repr__(self):
        return f'<Recipe {self.name}>'