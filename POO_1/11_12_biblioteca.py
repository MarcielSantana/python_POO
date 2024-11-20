class Biblioteca:
    def __init__(self, livros: list):
        self.livros = livros

    def adicionar_livros(self, nome):
        self.livros.append(nome)
        print(f"Livro '{nome}' adicionado com sucesso!")

    def remover_livro(self, nome):
        self.livros.remove(nome)

    def listar_livros(self):
        # Exibe todos os livros disponíveis
        print("Livros disponíveis na biblioteca:")
        for livro in self.livros:
            print(f"- {livro}")


biblioteca = Biblioteca(['Dom Quixote', '1984', 'A republica'])

# aqui está adicionando um livro a lista BIBLIOTECA
biblioteca.adicionar_livros('Hommo Deus')


# aqui está listando, mostrando os livros disponiveis
biblioteca.listar_livros()

# Aqui vou remover um livro que esteja na biblioteca
biblioteca.remover_livro('1984')
biblioteca.listar_livros()
