from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import configparser, uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

""" SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{database}".format(
    username=config.['db']['username'],
    password=config['db']['password'],
    hostname=config['db']['hostname'],
    databasename=config['db']['databasename']
) """

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
    app.run(debug=True)
    # app.run()

# TODO - Fazer com que o link apareça completo no retorno, e nao somente a key