#função escolha modelo, junto com os seus requisitos.
def escolhaModelo():
    modelos = {
        "MCS": ("Manga curta simples", 1.80),
        "MLS": ("Manga longa simples", 2.10),
        "MCE": ("Manga curta Com estampa", 2.90),
        "MLE": ("Manga longa Com estampa", 3.20)
}
    
    print('[Bem-vindo a Fabrica de camisetas do Vinicios Berudio de Oliveira]')
    print('---|Escolha o modelo desejado: ')


    for chave, value in modelos.items():
        print(f"{chave} - {value[0]}")
    print()

    while True:
        escolha = input()
        if escolha in modelos:
            return modelos[escolha][1]
        else:
            print('Escolha invalida, escolha o modelo novamente.')

#função de numero de camisetas, junto com os seus requisitos.
def num_camisetas():
    while True:
        try:
            num = int(input('Qual o numero de camisetas desejadas: '))
            if num > 2000:
                print('Não aceitamos pedido com essa quantidade de camisetas. Tente novamente...')
            else:
                break
        except ValueError:
            print('Entrada invalida. Por favor, entre com um numero valido.')

    if num < 20:
        desconto = 0.0
    elif 20 <= num < 200:
        desconto =  5 / 100
    elif 200 <= num < 2000:
        desconto = 7 / 100
    elif 2000 <= num <= 2000:
        desconto = 12 / 100

    return num, desconto

#função de frete, junto com os seus requisitos.
def frete():
    while True:
        try:
            opcao = int(input('Escolha o serviço de frete:\n1. Frete por transportadora  - R$100.00\n2. Sedex- R$200.00\n0. Retirar pedido na fabrica\n'))
            if opcao == 1:
                return 100.00
            elif opcao == 2:
                return 200.00
            elif opcao == 0:
                return 0.00
            else:
                print('Opção invalida. Escolha 1, 2 ou 0.')
        except ValueError:
            print('Opção invalida. por favor digite um numero.')

#Codigo principal
valorModelo = escolhaModelo()
num_camisetas, desconto = num_camisetas()
valorFrete = frete()
valorTotalCamisetas = num_camisetas * valorModelo *(1 - desconto)
valorTotal = valorTotalCamisetas + valorFrete

#imprimir todos os valores
print(f"O valor do modelo escolhido é: R$ {valorModelo:.2f}")
print(f"O número de camisetas escolhidas é: {num_camisetas}")
if desconto > 0:
    print(f"Você recebeu um desconto de {desconto * 100:.0f}% nas camisetas.")
print(f"O valor do frete escolhido é: R$ {valorFrete:.2f}")
print(f"Valor total a pagar: R$ {valorTotal:.2f}")