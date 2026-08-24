class Personagem():
    def __init__(self, nome, energia, ataque, ):
        self.nome = nome
        self.energia = energia
        self.ataque = ataque
        
        
        
personagens = []

personagem =  Personagem("P1", 100, 20)
personagens.append(personagem)
print("Seu personagem tem id:", len(personagens) -1)


personagem =  Personagem("P2", 80, 60)
personagens.append(personagem)
print("Seu personagem tem id:", len(personagens) -1)


print(personagens[0].nome)