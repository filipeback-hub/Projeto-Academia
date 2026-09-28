from classes import *

def l():
    print()

def titulo(tit):
    print(f'=== {tit} ===')


def menu():
    l()
    print('''===== ACADEMIA BACKEND =====
        ALUNOS
    1- Cadastrar aluno
    2- Listar alunos
    3- Buscar Aluno
    4- Editar Aluno
    5- Excluir Aluno
        PROFESSORES
    6- Cadastrar professor
    7- Listar Professores
    8- Buscar Professor
    9- Editar Professor
    10- Excluir professor
    
    11- Sair''')

    opcao = input('Escolha: ')
    return opcao

def cadastro_aluno(gym):
    titulo('CADASTRO DE ALUNO')
    nome = str(input('Nome: ')).strip().title()
    try:
        idade = int(input('Idade: '))
        gym.cadastrar_aluno(nome,idade)
    except ValueError:
        print('ERRO! Por favor digite um número valido')
    except PermissionError as erro:
        print(f'ERRO! {erro}')

def cadastro_professor(gym):
    titulo('CADASTRO DE PROFESSOR')
    nome = str(input('Nome: ')).strip().title()
    try:
        idade = int(input('Idade: '))
        gym.cadastrar_prof(nome,idade)
    except ValueError:
        print('ERRO! Por favor digite um número valido')
    except PermissionError as erro:
        print(f'ERRO! {erro}')

def listar_alunos(gym):
    titulo('LISTA DE ALUNOS')
    print(f'{'Matrícula':<10} {'Nome:':<20} {'Idade:':>5}')
    for aluno in gym.alunos:
        print(f'{aluno.matricula:<10} {aluno.nome:<20} {aluno.idade:>5}')

def listar_prof(gym):
    titulo('LISTA DE PROFESSORES')
    print(f'{'ID':<10} {'Nome:':<20} {'Idade:':>5}')
    for prof in gym.professores:
        print(f'{prof.id:<10} {prof.nome:<20} {prof.idade:>5}')

def buscar_aluno(gym):
    titulo('BUSCAR ALUNO')
    try:
        matricula = int(input('Matrícula do aluno: '))
        for alunos in gym.alunos:
            if matricula == alunos.matricula:
                print(f'Nome: {alunos.nome} ')
                print(f'Idade: {alunos.idade}')
                return
    except ValueError:
        print('ERRO! Por favor digite um número válido')
        return
    print('!Nenhum aluno encontrado!')

def buscar_prof(gym):
    titulo('BUSCAR PROFESSOR')
    try:
        id_prof = int(input('ID do professor: '))
        for prof in gym.professores:
            if id_prof == prof.id:
                print(f'Nome: {prof.nome} ')
                print(f'Idade: {prof.idade}')
                return
    except ValueError:
        print('ERRO! Por favor digite um número válido')
        return
    print('!Nenhum professor encontrado!')

def editar_aluno(gym):
    titulo('ALTERAR DADOS DO ALUNO')
    try:
        m = int(input('Matrícula do aluno: '))
        for a in gym.alunos:
            if m == a.matricula:
                print(f'Nome: {a.nome}')
                print(f'Idade: {a.idade}')
                nv_nome = input('Novo nome: ').strip().title()
                try:
                    nv_idade = int(input('Nova idade: '))
                    a.nome = nv_nome
                    a.idade = nv_idade
                    print('Alteração realizada com sucesso')
                    return
                except PermissionError as erro:
                    print(f'ERRO! {erro}')
                    return
                except ValueError:
                    print('ERRO! Por favor digite um número válido')
                    return
        print('Nenhum aluno encontrado!')
    except ValueError:
        print('ERRO! Por favor digite um número válido')

def editar_prof(gym):
    titulo('ALTERAR DADOS DO PROFESSOR')
    try:
        id_prof = int(input('ID do professor: '))
        for p in gym.professores:
            if id_prof == p.id:
                print(f'Nome: {p.nome}')
                print(f'Idade: {p.idade}')
                nv_nome = input('Novo nome: ').strip().title()
                try:
                    nv_idade = int(input('Nova idade: '))
                    p.nome = nv_nome
                    p.idade = nv_idade
                    print('Alteração realizada com sucesso')
                    return
                except PermissionError as erro:
                    print(f'ERRO! {erro}')
                    return
                except ValueError:
                    print('ERRO! Por favor digite um número válido')
                    return
        print('Nenhum professor encontrado!')
    except ValueError:
        print('ERRO! Por favor digite um número válido')

def excluir_aluno(gym):
    titulo('REMOVER ALUNO')
    try:
        matricula = int(input('Matrícula do aluno: '))
        for aluno in gym.alunos:
            if matricula == aluno.matricula:
                gym.alunos.remove(aluno)
                print(f'Aluno {aluno.nome} removido!!')
                return
        print('Nenhum aluno encontrado')
    except ValueError:
        print('ERRO! Por favor digite um número válido')

def excluir_prof(gym):
    titulo('REMOVER PROFESSOR')
    try:
        id_prof = int(input('ID do professor: '))
        for prof in gym.professores:
            if id_prof == prof.id:
                gym.professores.remove(prof)
                print(f'Professor {prof.nome} removido!!')
                return
        print('Nenhum professor encontrado')
    except ValueError:
        print('ERRO! Por favor digite um número válido')


def main():
    gym = Academia()
    while True:
        opc = menu()

        match opc:
            case '1':
                cadastro_aluno(gym)

            case '2':
                listar_alunos(gym)

            case '3':
                buscar_aluno(gym)

            case '4':
                editar_aluno(gym)

            case '5':
                excluir_aluno(gym)

            case '6':
                cadastro_professor(gym)

            case '7':
                listar_prof(gym)

            case '8':
                buscar_prof(gym)

            case '9':
                editar_prof(gym)

            case '10':
                excluir_prof(gym)

            case '11':
                break


if __name__ == '__main__':
    main()