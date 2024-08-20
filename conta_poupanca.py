from conta_bancaria import Conta_bancaria

class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, saldo, rendimento):
        super().__init__(titular, cpf, saldo)
        self.rendimento = rendimento

    def ver_rendimento(self):
        print(f"Taxa de rendimento: {self.rendimento * 100:.2f}% ao mês")

    def render(self):
        rendimento_valor = self.saldo * self.rendimento
        self.saldo += rendimento_valor
        print(f"Rendimento de R$ {rendimento_valor:.2f} aplicado ao saldo.")