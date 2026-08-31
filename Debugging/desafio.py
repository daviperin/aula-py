import logging as lg

lg.basicConfig(filename='arquivo_log.log',level=lg.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def calcular_pedido(cliente, produto,qtd, valor):
    try:
        if qtd <= 0 or valor <= 0:
            return ValueError('Quantidade = 0 ou valor negativo')
        
        lg.debug(f"Cliente: {cliente}\nProduto: {produto}\nValor: {valor}\n Quantidade: {qtd}")
        valor_final = qtd*valor
        
        print(f"Cliente: {cliente}\nProduto: {produto}\nValor Final: {valor_final}")
        lg.info("Pedido processado com sucesso")
        
    except ValueError as erro:
        lg.warning(erro)
        print('Pedido nao calculado, quantidade ou valor invalido')


def menu():
    lg.info('inicio do programa')

    while True:
        resposta = input("Digite 'sim' para calcular seu pedido ou 'nao' para terminar: ")

        if resposta == 'sim':
            cliente = input("Nome do cliente: ")
            produto = input("Nome do produto: ")
            
            try:
                qtd = int(input("Quantidade: "))
                valor = float(input("Valor: "))
            except ValueError:
                lg.warning('Quantidade ou valor digitado nao e um numero')
                
            calcular_pedido(cliente, produto, qtd,valor)
            
        elif resposta == 'nao':
            print('Programa finalizado')
            lg.info('Finalizando o Programa')
        else:
            lg.warning(f'Resposta invalida: {resposta}')
            print("Resposta invalida, digite 'sim' ou 'nao'")

menu()
