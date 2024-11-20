class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_bonus(self):
        bonus = self.salario + (self.salario * 10 / 100)
        print(f'''O salário do {self.nome} com bônus de 10% será de
        R$ {bonus:.2f}''')


funcionario = Funcionario('João', 'Gerente', 5000)

funcionario.calcular_bonus()
