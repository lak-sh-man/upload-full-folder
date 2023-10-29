#

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

"""@app.route("/", methods = ["GET"])
def home():
    return jsonify(
                    {"msg" : "Welcome",
                     "name" : "Lakshman"})"""

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    contact = db.Column(db.String(100), unique = True)

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'contact')

user_schema = UserSchema()
users_shema = UserSchema(many = True)

# Add new user 
@app.route('/User', methods = ["POST"])
def add_user():
    name = request.json["name"]
    contact = request.json["contact"]
    new_user = User(name, contact)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify

if __name__ == "__main__":
    app.run(debug = True, port = 5000)