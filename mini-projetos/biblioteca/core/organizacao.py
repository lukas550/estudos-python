# Módulo para a organização do main.py

def lin(char, qtd=30):
    print(char * qtd)

def menu(obj):
    if not isinstance(obj, dict):
        print("\nO objeto enviado não é um dicionário!\n")
    else:
        for i, opcao in obj.items():
            print(f"{i}. {opcao}")