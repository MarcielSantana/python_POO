class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def mostrar_preco(self):
        print(f'O(A) {self.nome} custa R$ {self.preco}')


produto = Produto('Coca-Cola', 8.99)

produto.mostrar_preco()
