from flask import Flask, jsonify, request
from routes.urls import routes
import psycopg2
import json

app = Flask(__name__)

app.register_blueprint(routes)