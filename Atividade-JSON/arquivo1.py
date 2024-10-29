import json
import os

funcionarios = [
    {
        "nome": "Erick Wellington Dantas de Oliveira Gomes",
        "idade": 25,
        "profissao": "Entregador",
        "salario": 2000,
        "ativo": False,
        "contatos": {
            "email": "erickwellington@empresaexe.com",
            "celular": "(84) 910123489",
            "residencial": "(84) 909871234"
        }
    },
    {
        "nome": "Andriela Gleice Pereira da Silva",
        "idade": 26,
        "profissao": "Desenvolvedora Front-End",
        "salario": 5000,
        "ativo": True,
        "contatos":{
            "email": "andrielagleice@empresaexe.com",
            "celular": "(84) 956762390",
            "residencial": "(84) 900346789"
        }
    },
    {
        "nome": "Elouise da Costa Galdino",
        "idade": 25,
        "profissao": "Designer",
        "salario": 4000,
        "ativo": False,
        "contatos":{
            "email": "elouisegaldino@empresaexe.com",
            "celular": "(84) 967230071",
            "residencial": "(84) 900789327"
        }
    },
    {
       "nome": "Acsa Mirella da Silva Dantas",
       "idade": 25,
       "profissao": "Desenvolvedora Back-End",
       "salario":  5500,
       "ativo": True,
       "contatos":{
           "email": "acsamirella@empresaexe.com",
           "celular": "(84) 957894512",
           "residencial": "(84) 977459035"
       }
    }
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo2.json')


with open(SAVE_TO, 'w') as file:
    json.dump(funcionarios, file, indent=4)
    