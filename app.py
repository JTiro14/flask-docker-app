# Corrected version of your code:
from flask import Flask
from dotenv import load_dotenv, find_dotenv
import os
from flask_jwt_extended import JWTManager
from db import db
from flask_migrate import Migrate
from routes.user import user_bp
from routes.auth import auth_bp

app = Flask(__name__)

load_dotenv(find_dotenv())
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///flask-api-db.db")
db.init_app(app)
migrate = Migrate(app, db)
app.config['JWT_SECRET_KEY'] = os.environ.get("FLASK_KEY")
jwt = JWTManager(app)

app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5121)