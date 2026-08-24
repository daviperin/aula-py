class ingressos:
    def __init__(self,evento:str, preco:float):
        self.evento = evento
        self.preco = preco

    def __str__(self):
        return f"Ingresso para {self.evento} - R$ {self.calcular_preco():.2f}"

    def __repr__(self):
        return f"evento={self.evento!r}, preco={self.preco!r}"


class IngressoInteiro(ingressos):
    def calcular_preco(self):
        return self.preco


class MeiaEntrada(ingressos):
    def calcular_preco(self):
        return self.preco / 2


def menu():
    evento = input("Digite o nome do evento: ")
    preco = float(input("Digite o preço do ingresso inteiro: "))

    print("\nEscolha o tipo de ingresso:")
    print("1 - Inteira")
    print("2 - Meia-entrada")
    opcao = input("Opção: ")

    if opcao == "1":
        ingresso = IngressoInteiro(evento, preco)
    elif opcao == "2":
        ingresso = MeiaEntrada(evento, preco)
    else:
        print("Opção inválida.")
        return

    print("\n" + str(ingresso))
    print(repr(ingresso))


menu()
