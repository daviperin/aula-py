class Produto:
    def __init__(self, nome, preco=0, qtd=0):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        
    def add(self, qtd):
        self.qtd += qtd 
        print(f'Voce adicionou {qtd} novas unidades para {self.nome}!')
        print(f'Agora {self.nome} tem no total {self.qtd} unidades.')
        
    def diminuir_estoque(self, qtd):
        self.qtd -= qtd 
        print(f'Voce removeu {qtd} peças de {self.nome}!')
        print(f'Agora {self.nome} tem no total {self.qtd} unidades.')
        
    def valor_total(self):
        valor_total = self.qtd *self.preco
        print(f'O valor total desta peça é {valor_total}')
        
    def exibir(self):
        print(f'Nome do Produto: {self.nome}\nValor: {self.preco}\nQuantidade: {self.qtd}')
        
                
        
p1 = Produto('ferro', 2, 10)
p1.add(2)
p1.diminuir_estoque(3)
p1.valor_total()
p1.exibir()
barra = '-' *50
print(barra)

p2 = Produto('engrenagem', 56, 72)
p2.add(20)
p2.diminuir_estoque(34)
p2.valor_total()
p2.exibir()