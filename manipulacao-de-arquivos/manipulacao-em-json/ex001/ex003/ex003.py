import json

try:
    with open("usuarios.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Erro: {e}")
    dados = []

def salvar_arquivo(id, nome, status):
    objeto = {"id": id, "nome": nome, "ativo": status}
    dados.append(objeto)

    with open("usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)

# Menu principal
while True:
    print("Digite 1 para adicionar nomes ao arquivo e 2 para encerrar!")
    escolha = input("= ").strip()

    if escolha == "1":
        nome_do_usuario = input("Digite o nome de usuário: ").strip()
        id_do_usuario = (input("Digite o id: ")).strip()
        esta_ativo = input("Está ativo (sim/não): ").lower().strip()

        status_do_usuario = True if esta_ativo in ["sim", "ss", "s"] else False

        salvar_arquivo(id_do_usuario, nome_do_usuario, status_do_usuario)
        print("\nSalvo!\n")
    elif escolha == "2":
        print("\nEncrrando...\n")
        break
    else:
        print("\nDigite algo válido!\n")