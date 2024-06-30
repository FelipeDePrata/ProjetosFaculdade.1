print('Bem-vindo a livraria de Felipe José.')
print('-' * 40)
print('-' * 8 + 'Menu Principal' + '-' * 8)


lista_livro = []
id_global = 0

def cadastrar_livro(id_global):
    dados_livros = {'Livro': ' ', 'Autor': ' ', 'Editora': ' '}
    dados_livros['ID'] = id_global
    dados_livros['Livro'] = str(input('Nome do livro: '))
    dados_livros['Autor'] = str(input('Autor: '))
    dados_livros['Editora'] = str(input('Editora: '))
    lista_livro.append(dados_livros.copy())

    while True:
        print(' ' * 100)
        print('-' * 8 + 'Menu de Cadastro.' + '-' * 8)
        cad = input('Deseja cadastrar mais algum livro?(S/N) ')
        if cad != 'S' and cad != 'N':
            print('Inválido. Tente novamente.')
            continue
        elif cad == 'S':
            id_global += 1
            cadastrar_livro(id_global)
        elif cad == 'N':
            print(' ' * 100)
            print('Retornando ao menu principal')
        break

def consultar_livro():
    while True:
        print('-' * 8 + 'Menu de Consulta.' + '-' * 8)
        print('1 - Consultar todos os livros.')
        print('2 - Consultar livros por ID.')
        print('3 - Consultar livros por autor.')
        print('4 - Retornar ao menu.')
        escolha = input('O que você deseja fazer? ')
        print(' ' * 100)
        if escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4':
            print('Escolha inválida. Tente novamente.')
            continue
        if escolha == '1':
            if lista_livro:
                for Livro in lista_livro:
                    print("ID:", Livro["ID"])
                    print("Livro:", Livro["Livro"])
                    print("Autor:", Livro["Autor"])
                    print("Editora:", Livro["Editora"])
                    print(' ' * 100)
        elif escolha == '2':
            id_escolha = int(input('Digite o ID do livro: '))
            if lista_livro:
                for ID in lista_livro:
                    if ID["ID"] == id_escolha:
                        print("ID:", ID["ID"])
                        print("Livro:", ID["Livro"])
                        print("Autor:", ID["Autor"])
                        print("Editora:", ID["Editora"])
                        print(' ' * 100)
        elif escolha == '3':
            Autor = input('Digite o nome do autor: ')
            if lista_livro:
                for Blake in lista_livro:
                    if Blake["Autor"] == Autor:
                        print("ID:", Blake["ID"])
                        print("Livro:", Blake["Livro"])
                        print("Autor:", Blake["Autor"])
                        print("Editora:", Blake["Editora"])
                        print(' ' * 100)
        elif escolha == '4':
            print('Retornando ao menu principal.')
            break


def remover_livro():
    while True:
            print('-' * 8 + 'Menu de Remoção.' + '-' * 8)
            D = int(input('Qual é o ID do livro que você deseja remover? '))
            if lista_livro:
                for Livro in lista_livro:
                    if Livro["ID"] == D:
                        lista_livro.remove(Livro)
                        print('Livro removido com sucesso.')
                        break
            else:
                print('ID inexistente. Tente novamente.')





while True:
    print('1. Cadastrar livro.')
    print('2. Consultar livro.')
    print('3. Remover livro.')
    print('4. Encerrar Programa.')
    x = input('O que você deseja? ')
    print(' ' * 100)
    if x != '1' and x != '2' and x != '3' and x != '4':
        print('Escolha inválida. Tente novamente.')
        continue
    elif x == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif x == '2':
        consultar_livro()
    elif x == '3':
        remover_livro()
    else:
        print('Encerrando o programa...')
        break