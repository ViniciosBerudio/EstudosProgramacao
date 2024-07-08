#print com o menu
print('[Bem-vindo à Loja de Marmitas do Vinicios Berudio de Oliveira]')
print('-' * 26 + 'Cardápio' + '-' * 26)
print('---| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) |---')
print('---| P       | R$ 16.00            | R$ 15.00            |---')
print('---| M       | R$ 18.00            | R$ 17.00            |---')
print('---| G       | R$ 22.00            | R$ 21.00            |---')
print('-' * 61)

valorTotal = 0

while True:
    #Validando as escolha de sabor e tamanho
    while True:
        sabor = input('Escolha qual sabor você quer? (BA/FF) ')
        if sabor  in ['BA', 'FF']:
            break
        else:
            print('Sabor invalido!\nTente novamente.')

    while True:
        tamanho = input('Qual tamanho do seu prato? (P,M,G) ')
        if tamanho in ['P', 'M', 'G']:
            break
        else:
            print('Tamanho errado!\nTente novamente!')

#adicionando os preços e sabores e implimentando o if elif aninhado
    if sabor == 'BA':
        if tamanho == 'P':
            valor = 16
        elif tamanho == 'M':
            valor = 18
        elif tamanho == 'G':
            valor = 22
    elif sabor == 'FF':
        if tamanho == 'P':
            valor = 15
        elif tamanho == 'm':
            valor = 17
        elif tamanho == 'G':
            valor = 21

#acumulador
    valorTotal += valor

    print(f'Voce pediu um {sabor} no tamanho {tamanho}: {valor:.2f}')
#perguntando se o cliente quer fazer mais um pedido e implimentando o while, break e continue
    while True:
        maisPedido =  input('Deseja pedir mais alguma coisa? (S/N)')
        if maisPedido == 'S':
            break
        elif maisPedido == 'N':
            break
        else:
            print('Resposta invalida! Digite "S" ou "N". ')
            continue

    if maisPedido == 'N':
        break

print(f'O valor total a ser pago ficou de {valorTotal:.2f}')