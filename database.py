from flask_sqlalchemy import SQLAlchemy
import configparser

config = configparser.ConfigParser()

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{database}".format(
    username=config.['db']['username'],
    password=config['db']['password'],
    hostname=config['db']['hostname'],
    databasename=config['db']['databasename']
)

class Pastes(db.Model):
    __tablename__ ="pastes"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)