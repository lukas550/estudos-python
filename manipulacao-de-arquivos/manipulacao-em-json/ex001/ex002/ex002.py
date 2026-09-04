import json

configuracoes = {
    "idioma": "Português",
    "tema": "Um tema",
    "notificacoes_ativas": None
}

with open("config.json", "w", encoding="utf-8") as arquivo:
    json.dump(configuracoes, arquivo, ensure_ascii=False, indent=4)

try:
    with open("config.json", "r", encoding="utf-8") as arquivo:
        configuracao = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Erro: {e}")

print(configuracao)