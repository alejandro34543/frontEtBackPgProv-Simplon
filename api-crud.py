"""
python 3.7

API 1 --  to read, update and delete the SQL database

John Armitage, Axel Alves 3/12/2019
"""
#"testetetstetestetssteetst"

import sqlalchemy
import json
import os
import base64
from flask import *
from flask_cors import CORS
from os import path

# HOME is a key within an environment file that points to the json file
pathFile = os.environ['HOME']
# pathFile = base64.b64decode(pathFileEncoded).decode('ascii') not necessary !?
pathFile = pathFile.rstrip()  # using opaque in secret requires me to strip the '\n'

app = Flask(__name__)

# _______________ Fonctions ____________
def readData():
    with open(pathFile) as json_file:
        datafile = json.load(json_file)
    return datafile


def putData(data):
    if path.exists(pathFile):
        with open(pathFile) as json_file:
            datafile = json.load(json_file)

        jdata = json.loads(data)
        adata = jdata["test2"]
        datafile["test2"].append(adata)

        with open(pathFile, 'w') as outfile:
            json.dump(datafile, outfile)
        process = True
    else:
        process = False
    return str(process)


def delData(articleid):
    if path.exists(pathFile):
        datafile = readData()
        datafile["test2"].pop(int(articleid))

        with open(pathFile, 'w') as outfile:
            json.dump(datafile, outfile)
        process = True
    else:
        process = False
    return str(process)


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
    print(str(data))
    result = putData(data)
    return result


@app.route('/data/<articleid>', methods=['DELETE'])
def parse_reqdel(articleid):
    result = delData(articleid)
    return 'You are deleting ' + articleid + ' : ' + result


if __name__ == '__main__':
    app.run("0.0.0.0")
