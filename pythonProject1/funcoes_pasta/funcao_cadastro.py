from main import Pessoa

def cadastro_pesso():
    nome=str(input("Digite o seu nome: "))
    idade=int(input("Digite a sua idade: "))
    gmail=str(input("Digite o seu melhor gmail: "))

    pessoa=Pessoa(nome, gmail, idade)
    print(f"\n")
    print(f"Nome: {pessoa.nome}")
    print(f"Idade: {pessoa.idade}")
    print(f"Gmail: {pessoa.gmail}")
    return idade






















