class Termometro:

    def __init__(self, temperatura: float):
        self.temperatura = temperatura

    def aumentar(self, valor):
        self.temperatura += valor

    def diminuir(self, valor):
        self.temperatura -= valor

    def mostrar_temperatura(self):
        print(f'A temperatura nesse momento está {self.temperatura} graus')


# mostrando a temperatura atual
termometro = Termometro(20)
termometro.mostrar_temperatura()

# mostrando a temperatura aumentando em 5
termometro.aumentar(5)
termometro.mostrar_temperatura()

# mostrando a temperatura diminuindo em 6
termometro.diminuir(6)
termometro.mostrar_temperatura()
