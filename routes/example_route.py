from flask import Blueprint, request, jsonify
from models.mongo_model import create_mongo_entry
from models.mysql_model import create_mysql_entry

example_blueprint = Blueprint("example_routes", __name__)

@example_blueprint.route("/add_teacher", methods=["POST"])
def add_teacher():
    data = request.json
    # MongoDB entry
    mongo_id = create_mongo_entry(data)
    # MySQL entry
    mysql_id = create_mysql_entry(data)
    return jsonify({"mongo_id": str(mongo_id), "mysql_id": mysql_id})