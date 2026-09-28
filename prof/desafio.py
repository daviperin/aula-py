import random
from memory_profiler import profile

@profile
def gerar_vendas(n=300000):
    vendas = []

    for i in range(n):
        venda = {
            "cliente": random.randint(1, 3000),
            "produto": random.randint(1, 100),
            "valor": random.uniform(10, 1000)
        }

        vendas.append(venda)

    return vendas

@profile
def calcular_faturamento(vendas):
    total = 0

    for venda in vendas:
        total += venda["valor"]

    return total

@profile
def calcular_por_cliente(vendas):
    resultado = {}

    for cliente in range(1, 300):

        total = 0

        for venda in vendas:
            if venda["cliente"] == cliente:
                total += venda["valor"]

        resultado[cliente] = total

    return resultado

@profile
def encontrar_vendas_altas(vendas):
    vendas_altas = []

    for venda in vendas:
        if venda["valor"] >= 900:
            vendas_altas.append(venda.copy())

    return vendas_altas

@profile
def main():

    vendas = gerar_vendas()

    faturamento = calcular_faturamento(vendas)
    clientes = calcular_por_cliente(vendas)
    vendas_altas = encontrar_vendas_altas(vendas)

    print(f"Faturamento: R$ {faturamento:,.2f}")
    print(f"Clientes analisados: {len(clientes)}")
    print(f"Vendas acima de R$ 900: {len(vendas_altas)}")


if __name__ == "__main__":
    main()