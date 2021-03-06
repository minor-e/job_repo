from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
# Creating app
app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
Migrate(app, db)

from app import routes, models


