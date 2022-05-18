from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Pais

import json
import requests

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///datospaisese.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos
archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
# archivo = open("data/data-personas-001.json", "r")
# archivo = request.get("------------------.json")

# datos_json =  json.load(archivo) # paso los datos del archivo a json
data = archivo.json()
# documentos = datos_json[" "]

for info in data:
    print(info)
    print(len(info.keys()))
    fila = Pais(nombre_pais=info['CLDR display name'], capital=info['Capital'], continente=info['Continent'], \
            dial=info['Dial'],geoname_id=info['Geoname ID'],ITU=info['ITU'],Lenguajes=info['Languages'],\
                Dependencia=info['is_independent'])
    session.add(fila)


# confirmar transacciones

session.commit()
