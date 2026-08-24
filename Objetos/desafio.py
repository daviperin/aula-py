class Conta:
    def __init__(self, descricao, valor, vencimento, status="nao paga"):
        self.descricao = descricao
        self.valor = valor
        self.vencimento = vencimento
        self.status = status 
        
    def pagar(self):
        self.status = "paga"

  
        
def cadastrar():
    descricao = input("Descricao: ")
    valor = float(input("Valor: "))
    vencimento = input("Vencimento (dd/mm/aaaa): ")

    conta = Conta(descricao, valor, vencimento)
    contas.append(conta)
    print("Conta cadastrada com id:", len(contas) - 1)


def listar():
    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
        return

    for id in range(len(contas)):
        conta = contas[id]
        print(id, "-", conta.descricao, "| R$", conta.valor,
              "| vence em", conta.vencimento, "|", conta.status)


def pagar():
    listar()
    if len(contas) == 0:
        return

    id = int(input("Id da conta que deseja pagar: "))
    if id < 0 or id >= len(contas):
        print("Id invalido.")
        return

    contas[id].pagar()
    print("Conta", contas[id].descricao, "marcada como paga.")



contas = []



while True:
    print()
    print("1 - Cadastrar conta")
    print("2 - Listar contas")
    print("3 - Pagar conta")
    print("4 - Sair")
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        pagar()
    elif opcao == "4":
        break
    else:
        print("Opcao invalida.")
