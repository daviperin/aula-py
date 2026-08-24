class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depositado: {valor}. Novo saldo: {self.saldo}')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Sacado: {valor}. Novo saldo: {self.saldo}')
        else:
            print('Saldo insuficiente ou valor inválido.')

    def exibir_saldo(self):
        print(f'Saldo atual de {self.titular}: {self.saldo}')
        
        
conta1 = Conta("Carlos", 1000)
conta1.exibir_saldo()
conta1.depositar(500)
conta1.sacar(200)
conta1.exibir_saldo()

conta2 = Conta("Ana", 200)
conta2.exibir_saldo()
conta2.depositar(300)
conta2.sacar(100)
conta2.exibir_saldo()