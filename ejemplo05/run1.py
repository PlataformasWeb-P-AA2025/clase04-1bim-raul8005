import requests
import json

# Abrir el archivo JSON con los datos
with open('atp_tennis_couchdb.json', 'r', encoding='utf-8') as archivo_json:
    contenido = json.load(archivo_json)

# Nombre de la base de datos CouchDB
nombre_bd = "personas005"
endpoint = f"http://127.0.0.1:5984/{nombre_bd}"
cabeceras = {'Content-Type': 'application/json'}

# Recorrer cada documento y enviarlo a la base de datos
for documento in contenido['docs']:
    resultado = requests.post(endpoint, headers=cabeceras, json=documento)
    print(f"> Documento con ID '{documento['_id']}' enviado. Código HTTP: {resultado.status_code}")
