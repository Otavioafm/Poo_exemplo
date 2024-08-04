from main import Livros

def Lista_livro(idade_usuario):
    livros = [  # Lista de instâncias da classe Livros
        Livros("Nothing can hurt me", "David Goggins", True, 14),
        Livros("A Arte da Guerra - Sun Tzu", "Sun Tzu", False, 14),
        Livros("Mais esperto que o Diabo", "Napoleon Hill", True, 16),
        Livros("As leis da invencibilidade", "Ryuho Okawa", False, 18)
    ]

    for livro in livros:
        # Verifica se o livro está disponível para a idade do usuário
        if livro.restricaoIdade <= idade_usuario:
            print(f"\n")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Disponível: {'Sim' if livro.disponibilidade else 'Não'}")
            print(f"Restrição de Idade: {livro.restricaoIdade}")
