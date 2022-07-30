# * Hello world flask app.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from config.environment import db_URI
# ? Instantiate flask
# ? __name__ is going to be a different value depending on
# ? where you run flask from. If you run this directly,
# ? it will be '__main__'
app = Flask(__name__)

app.config["SQLALCHEMY_DATABSE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)
bcrypt = Bcrypt(app)


from controllers import 
# ? Make a very basic route to talk to...
# * This @ syntax is a 'Decorator'. This decorator tell us
# * Which route our function belong to (our path for this route)
@app.route("/hello")
def home():
    return { "hello": "world" }
