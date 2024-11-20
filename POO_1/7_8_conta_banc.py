class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def mostrar_saldo(self):
        print(f'Seu saldo atual é de R$ {self.saldo}')


# mostra o valor atual
deposito1 = Conta(50)
deposito1.mostrar_saldo()

# adiciona 300 ao saldo e mostra o novo valor
deposito1.depositar(300)
deposito1.mostrar_saldo()
