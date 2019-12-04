"""
python 3.7

API 1 --  to read, update and delete the SQL database

John Armitage, Axel Alves 3/12/2019
"""


import json
import os
import base64
from flask import *
from flask_cors import CORS
from os import path

from config import DATABASE_URI
from model import Base, compte

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()

app = Flask(__name__)
CORS(app)


# _______________ Fonctions ____________
# get
def readData():
    result = s.query(compte)
    data = []
    for i in result:
        test = {
            'ID': i.ID,
            'Name': i.Nom,
            'Owner': i.Owner,
            'Namespace': i.Namespace,
            'User': i.User,
            'Password': i.Password
        }
        data.append(test)
    return str(json.dumps(data))


# post
def putData(data):
    sqldata = json.loads(data)
    print(data)
    print(sqldata)
    tableEntry = compte(
                ID=int(sqldata["ID"]),
                Nom=sqldata["Nom"],
                Owner=sqldata["Owner"],
                User=sqldata["User"],
                Password=sqldata["Password"],
                Namespace=sqldata["Namespace"],
            )
    s.add(tableEntry)
    s.commit()


#Delete
def delData(numb):
    query = s.query(compte).filter_by(ID=numb)
    s.delete(query.one())
    s.commit()
    return "TRUE"

# _______________ ROUTES _______________


@app.route('/v1/hello-world')
def hello_world():
    return 'Hello World!'


@app.route('/data', methods=['GET'])
def parse_reqget():
    # Votre fonction pour lire les data d'un fichier
    data = readData()
    return data


@app.route('/data', methods=['POST'])
def parse_reqpost():
    data = request.data  # Le payload de votre requete
    print(data)
    putData(data)
    return 'True'


@app.route('/data/<articleid>', methods=['DELETE'])
def api_article(articleid):
    delData(articleid)
    return 'Vous avez supprimer ' + articleid


if __name__ == '__main__':
    app.run()
    #app.run("0.0.0.0")

