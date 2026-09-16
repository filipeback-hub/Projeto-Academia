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
        if aluno < 12:
            raise PermissionError ('Idade não permitida para cadastro de aluno (Idade minima: 12 anos)')
        self.alunos.append(aluno)
        print(f'Aluno {aluno.nome} cadastrado com sucesso')


    def cadastrar_prof(self,prof):
        if prof < 18:
            raise PermissionError ('Idade não permitida para cadastro de professor (Idade minima: 18 anos)')
        self.professores.append(prof)
        print(f'Professor {prof.nome} cadastrado com sucesso')