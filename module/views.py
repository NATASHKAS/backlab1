from flask import jsonify, request
from module import app

CATEGORIES = [
    {
        "id": 1,
        "name": "food"
    }
]

USERS = [
    {
        "id": 1,
        "name": "Natashka"
    }
]

NOTES = [
    {
        "id": 1,
        "user_id": 1,
        "category_id": 1,
        "time": "30/10/2022",
        "expenses": 1000
    }
]

@app.route("/users")
def get_users():
    return jsonify({"users": USERS})

@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})

@app.route("/notes")
def get_notes():
    return jsonify({"notes": NOTES})

@app.route("/usernotes")
def get_usernotes():
    id = request.args.get("userid")
    notes = []
    for note in NOTES:
        if note["user_id"] == int(id):
            notes.append(note)
    return jsonify({"notes": notes})

@app.route("/categorynotes")
def get_categorynotes():
    category_id = request.args.get("categoryid")
    user_id = request.args.get("userid")
    notes = []
    for note in NOTES:
        if note["category_id"] == int(category_id) and note["user_id"] == int(user_id):
            notes.append(note)
    return jsonify({"notes": notes})

@app.route("/adduser", methods=["POST"])
def create_user():
    request_data = request.get_json()
    for user in USERS:
        if (user["id"] == request_data["id"]):
            return "Please, enter another id"
    USERS.append(request_data)
    return request_data

@app.route("/addcategory", methods=["POST"])
def create_category():
    request_data = request.get_json()
    for category in CATEGORIES:
        if (category["id"] == request_data["id"]):
            return "Please, enter another id"
    CATEGORIES.append(request_data)
    return request_data

@app.route("/addnote", methods=["POST"])
def create_note():
    request_data = request.get_json()
    for note in NOTES:
        if (note["id"] == request_data["id"]):
            return "Please, enter another id"
    NOTES.append(request_data)
    return request_data
