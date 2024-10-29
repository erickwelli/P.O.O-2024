import json
import os


BASE_DIR = os.path.dirname(__file__)

JSON_FILE = os.path.join(BASE_DIR, 'arquivo2.json')

novo_funcionario = {
    "nome": "Yasmin da Silva Vitoriano Medeiros",
    "idade": 25,
    "profissao": "Gerente",
    "salario": 9000,
    "ativo": True,
    "contatos": {
        "email": "yasminvitoriano@empresaexe.com",
        "celular": "(84) 978450158",
        "residencial": "(84) 911672345"
    }
}


if os.path.exists(JSON_FILE):
    with open(JSON_FILE, 'r') as file:
        funcionariosnovos = json.load(file)  
else:
    funcionariosnovos = []  


funcionariosnovos.append(novo_funcionario)


with open(JSON_FILE, 'w') as file:
    json.dump(funcionariosnovos, file, indent=4)
