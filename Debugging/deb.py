import logging as lg

lg.basicConfig(level=lg.DEBUG)


def dividir(m,n):
    lg.info('A funcao foi chamada')
    try:
        resultado = m/n
        lg.info("resultado", resultado)
        return resultado
    except ZeroDivisionError:
        lg.info('erro: divisao por 0')
        return 0
    
    
print(dividir(1,0))