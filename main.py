from classes import *

def menu():
    print('''==== ACADEMIA BACKEND ====
    1- Cadastrar aluno
    2- Cadastrar professor
    3- Listar alunos
    4- Listar Professores
    5- Sair''')

    opcao = input('Escolha: ')
    return opcao

def cadastro_aluno():
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    aluno = Aluno(nome,idade)
    gym = Academia()
    gym.cadastrar_aluno(aluno)

def cadastro_professor():
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    prof = Professor(nome,idade)
    gym = Academia()
    gym.cadastrar_prof(prof)


def main():
    while True:
        opc = menu()
        print(f'Opção escolhida: {opc}')

        if opc == '1':
            cadastro_aluno()

        if opc == '2':
            cadastro_professor()


        if opc == '5':
            break


if __name__ == '__main__':
    main()