from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import NOTES, USERS, CATEGORIES
from schemas import NoteSchema, NoteQuerySchema

blp = Blueprint("note", __name__, description="Operations on record")


@blp.route("/note")
class NoteList(MethodView):
    @blp.arguments(NoteQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, NoteSchema(many=True))
    def get(self, **kwargs):
        user_id = kwargs.get("user_id")
        category_id = kwargs.get("category_id")
        notes = []
        if not user_id:
            abort(400, message="Need at least user_id")
        if category_id:
            for note in NOTES:
                if (
                        note["category_id"] == int(category_id)
                        and note["user_id"] == int(user_id)
                ):
                    notes.append(note)
            return notes
        for note in NOTES:
            if note["user_id"] == int(user_id):
                notes.append(note)
        return notes


    @blp.arguments(NoteSchema)
    @blp.response(200, NoteSchema)
    def post(self, request_data):
        if request_data["id"] in [u["id"] for u in NOTES]:
            abort(400, message="ID must be unique")
        if request_data["user_id"] not in [u["id"] for u in USERS]:
            abort(400, message="User not found")
        if request_data["category_id"] not in [u["id"] for u in CATEGORIES]:
            abort(400, message="Category not found")
        NOTES.append(request_data)
        return request_data