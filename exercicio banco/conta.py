class Conta:

    def __init__(self, numero, saldo, limite):
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def sacar(self, saque):
        self.saldo -= saque

    def deposito(self, quantia):
        self.saldo += quantia
