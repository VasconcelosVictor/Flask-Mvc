from flask import Flask
from src.main.routes.person_routes import person_routes_bp

app = Flask(__name__)

app.register_blueprint(person_routes_bp)