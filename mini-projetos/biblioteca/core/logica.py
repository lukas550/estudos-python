# Módulo para a lógica do CRUD em main.py

def adicionar_livro(titulo, autor, ano):
    if not titulo.strip() or not autor.strip() or not ano.strip():
        raise ValueError("Uma informação está faltando")
        
    if not ano.isdigit() or len(ano) != 4:
        raise ValueError(f"O ano '{ano}' é inválido (deve conter 4 dígitos numéricos)")

    livro = {
            "titulo": titulo, 
            "autor": autor.lower(), 
            "ano": ano, 
            "lido": False
        }

    return livro

def listar_livros(biblioteca):
    if not biblioteca:
        print("\nA biblioteca está vazia!\n")
    else:
        for livro in biblioteca:
            status = "Lido" if livro["lido"] else "Não lido"

            print(f"- {livro['titulo']} | Autor: {livro['autor'].title()} | {livro['ano']} | {status}")

def busca_por_autor(autor, biblioteca):
    if not biblioteca:
        print("\nA biblioteca está vazia!\n")
    else:

        for livro in biblioteca:
            if livro["autor"] == autor.lower().strip():
                status = "Lido" if livro["lido"] else "Não lido"

                print(f"- {livro['titulo']} | Autor: {livro['autor'].title()} | {livro['ano']} | {status}")

def marcar_livro(livro, biblioteca):
    if not biblioteca:
        print("\nA biblioteca está vazia!\n")
    else:
        encontrou_livro = False

        for livrinho in biblioteca:
            if livrinho["titulo"].lower().strip() == livro.lower().strip():
                encontrou_livro = True

                if livrinho['lido']:
                    print(f"\nO livro {livrinho['titulo']} já foi marcado como lido!\n")
                else:
                    livrinho["lido"] = True

                    print(f"\nO livro {livrinho['titulo']} foi marcado como lido!\n")

        if not encontrou_livro:
            print(f"\nO livro {livro} não foi encontrado!\n")

def gerar_relatorio(biblioteca):
    if not biblioteca:
        print("\nA biblioteca está vazia!\n")
        return

    lidos = 0
    nao_lidos = 0

    for livro in biblioteca:
        if livro["lido"]:
            lidos += 1
        else:
            nao_lidos += 1

    total_de_livros = len(biblioteca)
    percentual = (lidos / total_de_livros) * 100
    mais_antigo = min(biblioteca, key=lambda x: int(x["ano"]))
    mais_recente = max(biblioteca, key=lambda x: int(x["ano"]))

    relatorio = {
        "total_de_livros": total_de_livros,
        "lidos": lidos,
        "nao_lidos": nao_lidos,
        "porcentagem": percentual,
        "mais_antigo": mais_antigo,
        "mais_recente": mais_recente
    }

    return relatorio