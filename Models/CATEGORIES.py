
from db import db


class CategoryModel(db.Model):
    tablename = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

    note = db.relationship("NoteModel", back_populates="category", lazy="dynamic")