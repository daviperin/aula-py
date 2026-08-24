class Aluno:
    def __init__(self, nome, _nota):
        self.nome = nome
        self.nota = _nota

    @property
    def nota(self):
        return self._nota

    def aprovado(self):
        if self._nota >= 6:
            print("Aprovado")
            return True
        elif self._nota < 6:
            print("Reprovado")
            return False


    @nota.setter
    def nota(self, valor):
        if valor >= 0 and valor <= 10:
            self._nota = valor
        else:
           raise ValueError('Nota nao pode ser negativa')

a1 = Aluno('estevao', 5)
print(a1.nome, a1.nota, a1.aprovado())