"""
Exercício 1
" Escreva um algoritmo que mostra, na tela,
quatro produtos a serem comprados em uma
lanchonete:
º Coxinha — R$ 5,00
º Pastel - R$ 7,00
º Café - R$ 4,00
º Suco - R$ 6,00
" Faça um algoritmo em que você seleciona o
produto que quer comprar e a quantidade.
Faça isso até que decida encerrar o programa

" Ao final, mostre o valor final do pedido a ser
pago
"""
print("LANCHONETE")
print("1 - Coxinha R$ 5.00")
print("2 - Pastel R$ 7.00")
print("3 - Café R$ 4.00")
print("4 - Suco R$ 6.00")
print("5 - Fechar pedido")

total = 0
while True:    
    op = int(input("Qual produto ira compra: "))
    qtd = int(input("Qual a quantidade: "))

    if (op == 1):
        total = total + qtd * 5.00
    elif (op == 2):
        total = total + qtd * 7.00
    elif (op == 3):
        total = total + qtd * 4.00
    elif (op == 4):
        total = total + qtd * 6.00
    elif (op == 5):
        break
    else:
        print("produto invalido. Selecione outro.")
#\n para pular uma linha
print(f"\nTotal a ser pago do seu pedido é de {total}.")