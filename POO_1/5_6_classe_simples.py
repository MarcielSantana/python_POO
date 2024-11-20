class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        print(f'Este carro é um "{self.marca}" modelo "{self.modelo}"')


carro = Carro('Ford', 'Ka 1.0')
carro.descrever()
