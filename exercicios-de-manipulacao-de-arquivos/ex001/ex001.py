# Agenda de contatos em arquivos .txt
try:
    with open("agenda.txt", "x") as agenda:
        pass
except FileExistsError:
    pass

print("\nSeus dados ficam salvos!\n")

opcoes = {
    "1": "Adicionar Contato",
    "2": "Listar Contatos",
    "3": "Remover Contato",
    "4": "Sair"
}

def menu():
    lin("-")
    for nu, opcao in opcoes.items():
        print(f"{nu} - {opcao}")
    lin("-")

def lin(char, qtd=30):
    print(char * qtd)

def adicionar_contato():
    novo_nome = input("Digite o nome do contato: ").lower().strip()
    while True:
        telefone = input(f"Digite o telefone de(a) {novo_nome.capitalize()}: ").strip()

        if not telefone.isdigit() or len(telefone) < 8:
            print("\nDigite no minímo oito números!\n")
        else:
            break
    
    return novo_nome, telefone

# Loop Principal
while True:
    menu()
    escolha = input("Escolha o número da opção que deseja: ")

    if escolha == "1":
        nome_do_contato, telefone_do_contato = adicionar_contato()

        try:
            with open("agenda.txt", "r", encoding="utf-8") as agenda:
                linhas = agenda.readlines()

                for linha in linhas:
                    nome_na_linha = linha.split("|")[0].strip()
                    if nome_do_contato == nome_na_linha:
                        escolha = input(f"{nome_do_contato} já existe. Deseja sobrescrever?\n").lower().strip()

                        if escolha not in ["sim", "ss", "s"]:
                            print("\nDados Preservados!\n")
                            break
                        else:

                            linhas_atualizadas = []
                            with open("agenda.txt", "r", encoding="utf-8") as agenda:
                                for linha in agenda:
                                    if nome_do_contato not in linha:
                                        linhas_atualizadas.append(linha)
                                linhas_atualizadas.append(f"{nome_do_contato} | {telefone_do_contato}")

                            with open("agenda.txt", "w", encoding="utf-8") as agenda:
                                agenda.writelines(linhas_atualizadas)
                            print("\nDados sobescritos!\n")
                            break

                else:
                    with open("agenda.txt", "a", encoding="utf-8") as agenda:
                        agenda.write(f"{nome_do_contato} | {telefone_do_contato}\n")

        except FileNotFoundError:
            print("\nArquivo não encontrado!\n")

    elif escolha == "2":
        lin('*')
        with open("agenda.txt", "r", encoding="utf-8") as agenda:
            linhas = []
            for linha in agenda:
                linhas.append(linha)

            if not linhas:
                print("\nSem conteúdo no arquivo!\n")
            else:
                for linha in linhas:
                    print(linha.strip().capitalize())
        lin('*')

    elif escolha == "3":
        contato_excluido = input("Digite o nome do contato que deseja excluir: ").strip().lower()
        linhas_filtradas = []

        with open("agenda.txt", "r", encoding="utf-8") as agenda:
            for linha in agenda:
                if contato_excluido not in linha:
                    linhas_filtradas.append(linha)

        with open("agenda.txt", "w", encoding="utf-8") as agenda:
            agenda.writelines(linhas_filtradas)

        print("\nContato excluído!\n")

    elif escolha == "4":
        print("\nEncerrando...\n")
        break

    else:
        print("\nDigite uma opção válida!\n")

# Feito com muito esforço e dedicação por Lukas!