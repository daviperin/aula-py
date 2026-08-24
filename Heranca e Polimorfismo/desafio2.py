from abc import ABC, abstractmethod

class Mensagem(ABC):
    def __init__(self,conteudo):
        self.conteudo = conteudo
        
    @abstractmethod
    def enviar():
        pass

class Email(Mensagem):
    def __init__(self, conteudo, destinatario):
        super().__init__(conteudo)
        self.destinatario = destinatario
        
    def enviar(self):
        return f"Enviando email para {self.destinatario}: {self.conteudo}"


class SMS(Mensagem):
    def __init__(self, conteudo, numero):
        super().__init__(conteudo)
        self.numero = numero
        
    def enviar(self):
        return f"Enviando SMS para {self.numero}: {self.conteudo}"


def menu():
    print("\nEscolha o tipo de mensagem que voce quer enviar:")
    print("1 - Email")
    print("2 - SMS")
    opcao = input("Opção: ")

    if opcao == "1":
        destinatario = input('Endereco de email do destinatario:')
        conteudo = input('Conteudo da mensagem:')
        mensagem = Email(conteudo, destinatario)
        print(mensagem.enviar())
    elif opcao == "2":
        destinatario = input('Numero do destinatario:')
        conteudo = input('Conteudo da mensagem:')
        mensagem = SMS(conteudo, destinatario)
        print(mensagem.enviar())
        
    else:
        print("Opção inválida.")
        return
    



menu()

