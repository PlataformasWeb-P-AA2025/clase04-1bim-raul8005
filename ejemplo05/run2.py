import requests
import json

# Cargar datos c docs
with open('atp_tennis_couchdb.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extraer lista documentos
solo_docs = data['docs']

# Base de datos 
base_datos = "personas006"
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar todos los documentos 
response = requests.post(url, headers=headers, json={"docs": solo_docs})

# Mostrar respuesta del servidor
print(response.status_code)
print(response.json())