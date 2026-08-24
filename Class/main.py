class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    
    def aniversario(self):
        self.idade += 1
        return f"Feliz aniversário, {self.nome}! Agora você tem {self.idade} anos."
    
p1 = Pessoa("João", 30)
print(p1.apresentar())
print(p1.aniversario())

p2 = Pessoa("Maria", 25)
print(p2.apresentar())
print(p2.aniversario())