import json

with open("arquivo.json", "r", encoding="utf-8") as arquivo_json:
    texto_json = arquivo_json.read()

# Método .loads() / string JSON para Objeto Python
dados_python = json.loads(texto_json)

print(dados_python)
print(type(dados_python))
print(dados_python["nome"])
print()

# Método .dumps() / Objeto python para String JSON
dados_json = json.dumps(dados_python)

print(dados_json)