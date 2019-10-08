from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

myGame = Flask(__name__)
myGame.config.from_object(Config)
db = SQLAlchemy(myGame)
migrate = Migrate(myGame, db)

from game import routes, models


