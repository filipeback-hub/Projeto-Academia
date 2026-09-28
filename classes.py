from abc import ABC

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
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self._matricula = matricula

    @Pessoa.idade.setter
    def idade(self,valor):
        if valor < 12:
            raise PermissionError('Idade não permitida para cadastro de aluno (Idade mínima: 12 anos)')
        self._idade = valor

    @property
    def matricula(self):
        return self._matricula


class Professor(Pessoa):
    def __init__(self, nome, idade, id_prof):
        super().__init__(nome, idade)
        self._id = id_prof

    @Pessoa.idade.setter
    def idade(self,valor):
        if valor < 18:
            raise PermissionError('Idade não permitida para cadastro de professor (Idade mínima: 18 anos)')
        self._idade = valor

    @property
    def id(self):
        return self._id


class Academia:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.cria_matriculas = 1001
        self.cria_id = 101


    def cadastrar_aluno(self,nome,idade):
        aluno = Aluno(nome,idade,self.cria_matriculas)
        self.alunos.append(aluno)
        print(f'Aluno {aluno.nome} cadastrado com sucesso')
        print(f'Matrícula do aluno: {aluno.matricula}')
        self.cria_matriculas += 1

    def cadastrar_prof(self,nome,idade):
        prof = Professor(nome,idade,self.cria_id)
        self.professores.append(prof)
        print(f'Professor {prof.nome} cadastrado com sucesso')
        print(f'ID do professor: {prof.id}')
        self.cria_id += 1