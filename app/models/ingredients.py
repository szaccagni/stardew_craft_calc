from app.extensions import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Ingredient {self.name}>'