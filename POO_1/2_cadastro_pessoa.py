# cadastrando uma pessoa

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos.')


pessoa = Pessoa('Marciel', 30)

pessoa.apresentar()
