from abc import ABC,abstractmethod

class Pessoa(ABC):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


class Professor(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)



class Academia:
    def __init__(self):
        self.alunos = []
        self.professores = []

    def cadastrar_aluno(self,aluno):
        self.alunos.append(aluno)
        print(f'Aluno {aluno.nome}({aluno.idade}) cadastrado com sucesso')


    def cadastrar_prof(self,prof):
        self.professores.append(prof)
        print(f'Professor {prof.nome}({prof.idade}) cadastrado com sucesso')