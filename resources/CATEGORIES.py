from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

from db import db
from Models import CategoryModel
from schemas import CategorySchema
from sqlalchemy.exc import IntegrityError

blp = Blueprint("category", __name__, description="Operations on category")


@blp.route("/category")
class CategoryList(MethodView):
    @jwt_required()
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @jwt_required()
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_data):
        category = CategoryModel(**request_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Name is taken")
        return category