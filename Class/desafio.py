class resenha:
    def __init__(self, nome, energia,ataque,moeda):
        self.nome = nome
        self.energia = energia
        self.ataque = ataque
        self.moeda =  moeda
        
    def atq(self,variavel):
        if variavel.energia <= 0:
            print(f'Seu oponente ja foi derrotado... Tenha misericórdia')
            return 
        variavel.energia = variavel.energia - self.ataque
        print(f'O {self.nome} deu {self.ataque} de dano!')
        print(f'Agora o {variavel.nome} esta com {variavel.energia} pontos de vida')
        if variavel.energia <= 0:
            print(f'{self.nome} WINS')
            print('FATALITY')
            print(f'{variavel.nome} foi derrotado, suas moedas irao ser passadas para o {self.nome}')
            self.moeda += variavel.moeda
            variavel.moeda = 0
            print(f'Agora o {self.nome} esta com o total de {self.moeda} moedas')
    
    
mago =resenha('Mago Patolino', 100, 50, 1000)
cavaleiro = resenha('Cavaleiro dos Zodiacos', 150, 25, 250)
mago.atq(cavaleiro)
mago.atq(cavaleiro)
mago.atq(cavaleiro)
mago.atq(cavaleiro)
mago.atq(cavaleiro)
mago.atq(cavaleiro)

        
        

