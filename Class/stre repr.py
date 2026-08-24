class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # __repr__: versao tecnica, para o programador/debug.
    # É usada por repr(obj), pelo console interativo, e dentro de listas/dicts.
    # Também é o fallback: se __str__ não existisse, print(obj) usaria esta aqui.
    def __repr__(self):
        return f"Pessoa(nome={self.nome!r}, idade={self.idade})"

    # __str__: versao amigavel, para o usuario final.
    # É usada por print(obj), str(obj) e f-strings/format.
    def __str__(self):
        return f"{self.nome}, {self.idade} anos"


if __name__ == "__main__":
    p = Pessoa("Davi", 30)

    print(p)          # chama __str__      -> Davi, 30 anos
    print(str(p))      # chama __str__      -> Davi, 30 anos
    print(repr(p))      # chama __repr__     -> Pessoa(nome='Davi', idade=30)

    lista = [p]
    print(lista)        # dentro de containers, usa __repr__ -> [Pessoa(nome='Davi', idade=30)]