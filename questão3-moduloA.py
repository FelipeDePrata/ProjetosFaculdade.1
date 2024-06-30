print('-' * 40)
print('Bem-vindo a Copiadora do Felipe José.')
print('-' * 40)
print('DIG - Digitalização - R$1.10/pag;')
print('ICO - Impressão Colorida - R$1/pag;')
print('IPB - Impressão Preto e Branco - R$ 0.40/pag;')
print('FOT - Fotocópia - 0.20/pag.')


def escolha_servico(): #Função para escolher o serviço.
    while True:
        serv = input('Qual serviço você deseja? ')
        if serv != 'DIG' and serv != 'ICO' and serv != 'IPB' and serv != 'FOT': #Validação
            print('Serviço inválido. Tente novamente. ')
            continue #looping até digitar um dos valores corretos.
        elif serv == 'DIG':
            serv = 1.10
        elif serv == 'ICO':
            serv = 1
        elif serv == 'IPB':
            serv = 0.40
        elif serv == 'FOT':
            serv = 0.20
        s1 = 'O serviço custará %.2f reais por cada página.'%serv
        print(s1)
        break #para brecar o loop
    return serv #retornar o valor da variável para a função.

def num_pagina(): #Função para escolher o serviço.
    while True:
        try: #Try/except para não dar erro no programa ao digitar caractere invés de int.
            pag = int(input('Quantas páginas você deseja? '))
            if pag < 20:
                print('Você não terá nenhum desconto. ')
                return pag
            if pag >= 20 and pag < 200: #Máximo e mínimo de páginas para o desconto.
                print('Você terá 15% de desconto. ')
                return pag * 15/100 #Retornando o valor do cálculo de desconto por página.
            if pag >= 200 and pag < 2000:
                print('Você terá 20% de desconto. ')
                return pag * 20/100
            if pag >= 2000 and pag < 20000:
                print('Você terá 25% de desconto. ')
                return pag * 25/100
            else:
                print('Não aceitamos pedidos com essa quantidade de páginas. ')
                continue #looping até digitar um dos valores corretos.
        except ValueError:
            print('Número inválido. Tente novamente. ')
            continue

def servico_extra(): #função para o serviço extra.
    while True: #loop
            print('1 - Encadernação simples - R$15')
            print('2 - Encadernação de capa dura - R$40')
            print('0 - Não, obrigado.')
            try: #try/except para evitar caractere ao invés de int.
                extra = int(input('Você deseja um serviço adicional? '))
                if extra != 1 and extra != 2 and extra != 0:
                    print('Valor inválido. Tente novamente.')
                    continue
                elif extra == 1:
                    extra = 15
                elif extra == 2:
                    extra = 40
                elif extra == 0:
                    extra = 0
                return extra
            except ValueError:
                print('Valor inválido. Tente novamente.')
                continue

servico = escolha_servico() #variável recebendo o retorno da função escolha_servico().
qtd = num_pagina() #variável recebendo o retorno da função num_pagina().
ex = servico_extra() #variável recebendo o retorno da função servico_extra().

total = (servico * qtd) + ex #o cálculo total com o retorno de todas as funções.

s1 = 'O serviço custará %.2f reais no total.'%total
print(s1) #print e string com o valor total do serviço.