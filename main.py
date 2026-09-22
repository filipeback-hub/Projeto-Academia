from classes import *

def l():
    print()

def titulo(tit):
    print(f'=== {tit} ===')


def menu():
    l()
    print('''===== ACADEMIA BACKEND =====
    1- Cadastrar aluno
    2- Cadastrar professor
    3- Listar alunos
    4- Listar Professores
    5- Buscar Aluno
    6- Buscar Professor
    7- Editar Aluno
    8- Editar Professor
    9- Excluir Aluno
    10- Excluir professor
    11- Sair''')

    opcao = input('Escolha: ')
    return opcao

def cadastro_aluno(gym):
    titulo('CADASTRO DE ALUNO')
    nome = str(input('Nome: ')).strip().title()
    try:
        idade = int(input('Idade: '))
        aluno = Aluno(nome,idade)
        gym.cadastrar_aluno(aluno)
    except ValueError:
        print('ERRO! Por favor digite um número valido')

def cadastro_professor(gym):
    titulo('CADASTRO DE PROFESSOR')
    nome = str(input('Nome: ')).strip().title()
    try:
        idade = int(input('Idade: '))
        prof = Professor(nome, idade)
        gym.cadastrar_prof(prof)
    except ValueError:
        print('ERRO! Por favor digite um número valido')

def listar_alunos(gym):
    titulo('LISTA DE ALUNOS')
    print(f'{'Nome:':<10}  {'Idade:':>10}')
    for aluno in gym.alunos:
        print(f'{aluno.nome:<10} {aluno.idade:>9}')

def listar_prof(gym):
    titulo('LISTA DE PROFESSORES')
    print(f'{'Nome:':<10}  {'Idade:':>10}')
    for prof in gym.professores:
        print(f'{prof.nome:<10} {prof.idade:>9}')

def buscar_aluno(gym):
    titulo('BUSCAR ALUNO')
    nome = input('Nome do aluno: ').strip().title()
    for alunos in gym.alunos:
        if nome == alunos.nome:
            print(f'Nome: {alunos.nome} ')
            print(f'Idade: {alunos.idade}')
            return
    print('!Nenhum aluno encontrado!')

def buscar_prof(gym):
    titulo('BUSCAR PROFESSOR')
    nome = input('Nome do professor: ').strip().title()
    for prof in gym.professores:
        if nome == prof.nome:
            print(f'Nome: {prof.nome} ')
            print(f'Idade: {prof.idade}')
            return
    print('!Nenhum professor encontrado!')

def editar_aluno(gym):
    titulo('ALTERAR DADOS DO ALUNO')
    nome = input('Nome do aluno: ').strip().title()
    for a in gym.alunos:
        if nome == a.nome:
            print(f'Nome: {a.nome}')
            print(f'Idade: {a.idade}')
            nv_nome = input('Novo nome: ').strip().title()
            nv_idade = int(input('Nova idade: '))
            a.nome = nv_nome
            a.idade = nv_idade
            print('Alteração realizada com sucesso')
            return
    print('Nenhum aluno encontrado!')

def editar_prof(gym):
    titulo('ALTERAR DADOS DO PROFESSOR')
    nome = input('Nome do professor: ').strip().title()
    for p in gym.professores:
        if nome == p.nome:
            print(f'Nome: {p.nome}')
            print(f'Idade: {p.idade}')
            nv_nome = input('Novo nome: ').strip().title()
            nv_idade = int(input('Nova idade: '))
            p.nome = nv_nome
            p.idade = nv_idade
            print('Alteração realizada com sucesso')
            return
        print('Nenhum professor encontrado!')

def excluir_aluno(gym):
    titulo('REMOVER ALUNO')
    nome = input('Nome do aluno: ').strip().title()
    for aluno in gym.alunos:
        if nome == aluno.nome:
            gym.alunos.revove(aluno)
            print(f'Aluno {aluno.nome} removido!!')
            return
    print('Nenhum aluno encontrado')

def excluir_prof(gym):
    titulo('REMOVER PROFESSOR')
    nome = input('Nome do professor: ').strip().title()
    for prof in gym.professores:
        if nome == prof.nome:
            gym.professores.remove(prof)
            print(f'Professor {prof.nome} removio!!')
            return
    print('Nenhum professor encontrado')


def main():
    gym = Academia()
    while True:
        opc = menu()

        match opc:
            case '1':
                cadastro_aluno(gym)

            case '2':
                cadastro_professor(gym)

            case '3':
                listar_alunos(gym)

            case '4':
                listar_prof(gym)

            case '5':
                buscar_aluno(gym)

            case '6':
                buscar_prof(gym)

            case '7':
                editar_aluno(gym)

            case '8':
                editar_prof(gym)

            case '9':
                excluir_aluno(gym)

            case '10':
                excluir_prof(gym)

            case '11':
                break


if __name__ == '__main__':
    main()