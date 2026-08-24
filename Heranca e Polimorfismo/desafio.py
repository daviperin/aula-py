class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade =  idade
     


class Aluno(Pessoa):
    def __init__(self, nome, idade,curso,matricula,):
        super().__init__(nome, idade)
        self.curso = curso
        self.matricula = matricula
        
    def descricao(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nMatricula {self.matricula}\nCurso: {self.curso} "
    
    
class Professor(Pessoa):
    def __init__(self, nome, idade,salario,disciplina,):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina
         
    def descricao(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nSalario {self.salario}\nDisciplina: {self.disciplina} "

    
    
aluno1 = Aluno('MISSE', 20, 'dadawdawdw', 'CINEMA')
professor1 = Professor('DAVI', 32, 200000, 'CAMERA CINEMA')

print(aluno1.descricao())
print(professor1.descricao())