import saudacao

nome = input("Digite seu nome: ").capitalize().strip()

print(f"\nIdioma: {saudacao.IDIOMA}\n")
print(saudacao.cumprimentar(nome))
print(saudacao.despedir(nome))