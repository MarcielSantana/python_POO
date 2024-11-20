class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos.')


pessoa = Pessoa('Marciel', 30)
pessoa.apresentar()

# Aqui está incrementando a idade da pessoa em 1
pessoa.fazer_aniversario()
pessoa.apresentar()
