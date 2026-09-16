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
    5- Sair''')

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



def main():
    gym = Academia()
    while True:
        opc = menu()

        if opc == '1':
            cadastro_aluno(gym)

        if opc == '2':
            cadastro_professor(gym)

        if opc == '3':
            listar_alunos(gym)

        if opc == '4':
            listar_prof(gym)

        if opc == '5':
            break


if __name__ == '__main__':
    main()