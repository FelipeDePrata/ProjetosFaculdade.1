print('Bem-vindo a Loja de Gelados do Felipe José.')
print('-' * 15 + 'Cardápio' + '-' * 15)
print('-' * 38)
print('-| Tamanho | Cupuaçu(CP) | Açaí(AC) |-' )
print('-| P ' + ' ' * 6 + '| R$ 9.00 ' + ' ' * 4 + '| R$11.00  |-')
print('-| M ' + ' ' * 6 + '| R$ 14.00 ' + ' ' * 3 + '| R$16.00  |-')
print('-| G ' + ' ' * 6 + '| R$ 18.00 ' + ' ' * 3 + '| R$20.00  |-')
print('-' * 38)

valor_Total = 0 # Acumulador

while True:
    sabor = input('Digite o sabor desejado(CP/AC): ')
    if sabor != 'CP' and sabor != 'AC':
        print('Sabor inválido. Digite novamente. ')
        continue
    #Caso o valor seja inválido, o continue irá voltar o loop ao início.

    tamanho = input('Digite o tamanho desejado(P/M/G): ')
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Digite novamente. ')
        continue
    #O loop também voltará ao início em caso de valor inválido.

    if sabor == 'CP' and tamanho == 'P':
            preco = 9.00
    elif sabor == 'CP' and tamanho == 'M':
                preco = 14.00
    elif sabor == 'CP' and tamanho == 'G':
            preco = 18.00
    elif sabor == 'AC' and tamanho == 'P':
            preco = 11.00
    elif sabor == 'AC' and tamanho == 'M':
            preco = 16.00
    elif sabor == 'AC' and tamanho == 'G':
            preco = 20.00
    valor_Total += preco
    #Os preços dos produtos escolhidos são somados ao valor_Total.

    continuar = input('Você deseja pedir algo mais?(S/N) ')
    if continuar == 'S':
        continue
    #Caso o cliente queira pedir algo a mais, o loop irá voltar a partir do sabor desejado.
    else:
        print(f'O valor total do seu pedido é: {valor_Total}')
    break
    #Por fim, o break encerra o programa com o total do pedido representado pelo acumulador.
