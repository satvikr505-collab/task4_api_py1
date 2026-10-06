from flask import Flask, request, jsonify

app = Flask(__name__)


# In-memory user data
users = [
    {
        "id": 1,
        "name": "Rahul",
        "email": "rahul@gmail.com"
    },
    {
        "id": 2,
        "name": "Priya",
        "email": "priya@gmail.com"
    }
]


# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Flask User REST API"
    })


# GET - Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# GET - Get a single user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200

    return jsonify({
        "error": "User not found"
    }), 404


# POST - Create a new user
@app.route("/users", methods=["POST"])
def create_user():

    data = request.json

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if "name" not in data or "email" not in data:
        return jsonify({
            "error": "Name and email are required"
        }), 400

    new_id = max([user["id"] for user in users], default=0) + 1

    new_user = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)

    return jsonify({
        "message": "User created successfully",
        "user": new_user
    }), 201


# PUT - Update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    data = request.json

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    for user in users:

        if user["id"] == user_id:

            if "name" in data:
                user["name"] = data["name"]

            if "email" in data:
                user["email"] = data["email"]

            return jsonify({
                "message": "User updated successfully",
                "user": user
            }), 200

    return jsonify({
        "error": "User not found"
    }), 404


# DELETE - Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            return jsonify({
                "message": "User deleted successfully"
            }), 200

    return jsonify({
        "error": "User not found"
    }), 404


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)