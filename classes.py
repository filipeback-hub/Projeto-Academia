from abc import ABC,abstractmethod

class Pessoa(ABC):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self,valor):
        self._idade = valor


class Aluno(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    @Pessoa.idade.setter
    def idade(self,valor):
        if valor < 12:
            raise PermissionError('Idade não permitida para cadastro de aluno (Idade minima: 12 anos)')
        self._idade = valor


class Professor(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    @Pessoa.idade.setter
    def idade(self,valor):
        if valor < 18:
            raise PermissionError('Idade não permitida para cadastro de professor (Idade minima: 18 anos)')
        self._idade = valor



class Academia:
    def __init__(self):
        self.alunos = []
        self.professores = []

    def cadastrar_aluno(self,aluno):
        self.alunos.append(aluno)
        print(f'Aluno {aluno.nome} cadastrado com sucesso')


    def cadastrar_prof(self,prof):
        self.professores.append(prof)
        print(f'Professor {prof.nome} cadastrado com sucesso')