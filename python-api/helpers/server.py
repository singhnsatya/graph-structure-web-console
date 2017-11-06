from flask import Flask, jsonify, request
from routes.urls import routes
from helpers.connection import connectDB
from flask_cors import CORS
import psycopg2
import json

app = Flask(__name__)
connectDB()
CORS(app)
app.register_blueprint(routes)