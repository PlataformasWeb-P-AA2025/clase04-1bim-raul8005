import csv
import json
import os
import uuid

# Ruta archivo CSV
csv_file = 'atp_tennis.csv'
json_file = 'atp_tennis_couchdb.json'

# Verifica existencia archivo
if not os.path.exists(csv_file):
    print(f"El archivo '{csv_file}' no se encontró.")
    exit(1)

data = []

# Lee CSV y convierte a documento JSON
try:
    with open(csv_file, newline='', encoding='latin1') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # id unico
            row['_id'] = str(uuid.uuid4())  
            data.append(row)
except Exception as e:
    print(f"Error al leer el CSV: {e}")
    exit(1)


output = {"docs": data}

try:
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
    print(f"Archivo JSON generado  y guardado como: '{json_file}' ")
except Exception as e:
    print(f"Error al guardar el JSON: {e}")