from core import arquivo, logica, organizacao

arquivo.criar_biblioteca() # Cria biblioteca
arquivo.criar_relatorio() # Cria relatório
biblioteca = arquivo.carregar_biblioteca() # Carrega biblioteca
relatorio = arquivo.carregar_relatorio() # Carrega relatório

opcoes = {
    "1": "Adicionar livro",
    "2": "Listar Livros",
    "3": "Busca por Autor",
    "4": "Marcar como Lido",
    "5": "Relatório",
    "6": "Sair"
}

while True:
    organizacao.lin("-")
    organizacao.menu(opcoes)
    organizacao.lin("-")

    escolha = input("Digite o número da opção que deseja: ").strip()
    if escolha == "1":

        organizacao.lin("-")
        while True:
            
            try:
                nome_do_livro = input("\nDigite o nome do livro que deseja cadastrar: ")
                autor_do_livro = input(f"Digite o nome do autor de {nome_do_livro}: ")
                ano_do_livro = input(f"Digite o ano da obra {nome_do_livro}: ")

                livro_salvo = logica.adicionar_livro(nome_do_livro, autor_do_livro, ano_do_livro)
            except ValueError as e:
                print(f"\n{e}, tente novamente!\n")
            else:
                biblioteca.append(livro_salvo)

                arquivo.salvar_biblioteca(biblioteca)
                break
        print(f"\nLivro {nome_do_livro} foi salvo!\n")
        organizacao.lin("-")

    elif escolha == "2":

        print()
        organizacao.lin("*")
        logica.listar_livros(biblioteca)
        organizacao.lin("*")
        print()
        
    elif escolha == "3":

        autor_procurado = input("\nDigite o nome do autor procurado: ")

        organizacao.lin("*")
        logica.busca_por_autor(autor_procurado, biblioteca)
        organizacao.lin("*")
        print()
        
    elif escolha == "4":

        organizacao.lin("-")
        livro_procurado = input("\nDigite o nome do livro procurado: ")

        logica.marcar_livro(livro_procurado, biblioteca)
        arquivo.salvar_biblioteca(biblioteca)
        organizacao.lin("-")        
        
    elif escolha == "5": # TODO: Fazer opção 5

        organizacao.lin("-")
        relatorio = logica.gerar_relatorio(biblioteca)

        if relatorio:
            arquivo.salvar_relatorio(relatorio)

            print("\n===== RELATÓRIO DA BIBLIOTECA =====")
            print(f"Total de Livros: {relatorio['total_de_livros']}")
            print(f"Livros Lidos: {relatorio['lidos']} | {relatorio['porcentagem']}%")
            print(f"Livros Não Lidos: {relatorio['nao_lidos']}")
            print(f"Mais Antigo: {relatorio['mais_antigo']['titulo']}")
            print(f"Mais Recente: {relatorio['mais_recente']['titulo']}")
            print("===================================\n")

        else:
            print("\nSem relatório!\n")

        organizacao.lin("-")

    elif escolha == "6":
    
        print("\nEncerrando...\n")
        break

    else:
        print("\nDigite algo válido!\n")