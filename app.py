from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import mysql.connector
from config import MONGO_URI, MYSQL_CONFIG

app = Flask(__name__)
CORS(app)

# MongoDB setup
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["shiksha_mitra"]

# MySQL setup
mysql_conn = mysql.connector.connect(**MYSQL_CONFIG)
mysql_cursor = mysql_conn.cursor()

# Import routes
from routes.example_route import example_blueprint
app.register_blueprint(example_blueprint)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to Shiksha Mitra Backend!"})

if __name__ == "__main__":
    app.run(debug=True)