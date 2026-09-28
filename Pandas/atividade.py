from abc import ABC, abstractmethod
from datetime import datetime

class Chamado(ABC):
    def __init__(self,titulo,descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = "Aberto"
        self.data_abertura = datetime.now().strftime("%d/%m/%Y %H:%M")
        
    @abstractmethod
    def exibir_resumo(self):
        pass
        
        
class Hardware(Chamado):
    def __init__(self,titulo,descricao,patrimonio):
        super().__init__(titulo,descricao)
        self.patrimonio = patrimonio
        
    def exibir_resumo(self):
        return f"Hardware {self.titulo} - Descrição: {self.descricao} - Patrimonio: {self.patrimonio} - Status: {self.status}"
    
class Software(Chamado):
    def __init__(self,titulo,descricao,sistema):
        super().__init__(titulo,descricao)
        self.sistema = sistema
        
    def exibir_resumo(self):
        return f"Software {self.titulo} - Descrição: {self.descricao} - Sistema: {self.sistema} - Status: {self.status}"

chamados = []

def abrir_hardware():
    titulo = input("Titulo do chamado: ")
    descricao = input("Descricao: ")
    patrimonio = input("Patrimonio do equipamento: ")
    
    chamado = Hardware(titulo,descricao,patrimonio)
    chamados.append(chamado)
    
    print("Chamado de Hardware aberto com sucesso.")
    
def abrir_software():
    titulo = input("Titulo do chamado: ")
    descricao = input("Descricao: ")
    sistema = input("Sistema (ex.: ERP X, Windows): ")
    
    chamado = Software(titulo,descricao,sistema)
    chamados.append(chamado)
    
    print("Chamado de Software aberto com sucesso.")
    
def listar(lista,tipo):
    if not lista:
       print("Nenhum chamado encontrado.")
       return
   
    if tipo == "todos":
        print("Todos os chamados:")
        for chamado in lista:
            print(chamado.exibir_resumo())
            
    if tipo == "hardware":
         print("Chamados de Hardware:")
         for chamado in lista:
             if isinstance(chamado, Hardware):
               print(chamado.exibir_resumo())
               
    elif tipo == "software":
         print("Chamados de Software:")
         for chamado in lista:
             if isinstance(chamado, Software):
               print(chamado.exibir_resumo())

def menu():
    while True:
        print("Sistema de Chamados")
        print("1) Abrir chamado de Hardware")
        print("2) Abrir chamado de Software")
        print("3) Listar chamados Hardware")
        print("4) Listar chamados Software")
        print("5) Listar todos os chamados")
        print("6) Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            abrir_hardware()
        elif opcao == "2":
            abrir_software()
        elif opcao == "3":
            listar(chamados,"hardware")
        elif opcao == "4":
            listar(chamados,"software")
        elif opcao == "5":
            listar(chamados,"todos")
        elif opcao == "6":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
menu()