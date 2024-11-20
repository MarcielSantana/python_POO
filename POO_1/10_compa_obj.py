class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome}, {self.preco}'

    def eh_mais_barato(self, outro_produto):
        return self.preco < outro_produto.preco


produto1 = Produto('Coca-Cola', 9.99)

produto2 = Produto('Kuat', 6.99)

if produto1.eh_mais_barato(produto2):
    print(f'''produto 1: {produto1.nome} é mais barato que o
        produto 2: {produto2.nome}''')
else:
    print(f'''produto 2: {produto2.nome} é mais barato que o
        produto 1: {produto1.nome}''')
