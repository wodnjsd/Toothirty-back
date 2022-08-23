
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from config.environment import db_URI

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)
bcrypt = Bcrypt(app)


from controllers import advice, problems, types, users

app.register_blueprint(advice.router, url_prefix="/api")
app.register_blueprint(problems.router, url_prefix="/api")
app.register_blueprint(types.router, url_prefix="/api")
app.register_blueprint(users.router, url_prefix="/api")
