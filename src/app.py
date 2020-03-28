import configparser
import uuid
import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)


class Pastes(db.Model):
    __tablename__ ="pastes"
    id      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key     = db.Column(db.String(36))
    content = db.Column(db.Text)

    def __init__(self, key, content):
        self.key = key
        self.content = content


db.create_all()


@app.route("/")
@app.route("/home")
def index():
    return render_template("editor.html")

@app.route("/saveContent", methods=["POST"])
def saveContent():
        content = request.form.get('content')
        key = str(generateKey())
        paste = Pastes(key, content)
        db.session.add(paste)
        db.session.commit()
        return jsonify({'sucess' : True, 'key' : key})

@app.route("/<key>")
def getPaste(key):
    paste = Pastes.query.filter_by(key=key).first()
    return render_template("editor.html", content=paste.content)

def generateKey():
    return uuid.uuid4()

if __name__ == '__main__':
    # app.run(debug=True)
    port = os.getenv('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
