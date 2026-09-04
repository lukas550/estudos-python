#  Módulo para salvar os arquivos, carregar e criar, utliza json.
import json
"""
Estrutura de um arquivo:
[
    {
        "titulo": str (nome do livro),
        "autor": str (nome do autor),
        "ano": int,
        "lido": bool,
    }
]
"""


ARQUIVO = "biblioteca.json"
ARQUIVO_2 = "relatorio.json"

# Funções Biblioteca

def salvar_biblioteca(dados_a_salvar):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(dados_a_salvar, f, ensure_ascii=False, indent=4)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"\nErro no salvamento do arquivo: {e}\n")

def carregar_biblioteca():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados_da_biblioteca = json.load(f)

        return dados_da_biblioteca
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro em carregar o arquivo: {e}")

        return []

def criar_biblioteca():
    try:
        with open(ARQUIVO, "x", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
            print("\nArquivo foi criado!\n")
    except FileExistsError:
        pass

# Funções Relatório

def salvar_relatorio(relatorio):
    try:
        with open(ARQUIVO_2, "w", encoding="utf-8") as f:
            json.dump(relatorio, f, ensure_ascii=False, indent=4)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro no salvamento do arquivo: {e}\n")

def carregar_relatorio():
    try:
        with open(ARQUIVO_2, "r", encoding="utf-8") as f:
            dados_do_relatorio = json.load(f)

            return dados_do_relatorio
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"\nErro em carregar o arquivo: {e}\n")

        return {}

def criar_relatorio():
    try:
        with open(ARQUIVO_2, "x", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
            print("Arquivo foi criado!\n")

    except FileExistsError:
        pass