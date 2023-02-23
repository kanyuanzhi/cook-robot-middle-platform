from sqlite_db import db
from db_model.base import BaseDbModel


class IngredientDbModel(BaseDbModel):
    __tablename__ = "ingredients"
    name = db.Column(db.String, nullable=False, default="")
    classification = db.Column(db.String, nullable=False, default="")

    def __init__(self, name, classification):
        super(IngredientDbModel, self).__init__()
        self.name = name
        self.classification = classification

    def __repr__(self):
        return '<Ingredient %r>' % self.name
