import json
import os

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo2.json')

with open(JSON_FILE, 'r') as file:
    funcionarios = json.load(file)
    
    for funcionario in funcionarios:
        print(funcionario)