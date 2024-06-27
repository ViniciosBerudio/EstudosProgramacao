'''
Crie um programa que leia quanto dinheiro tem na carteira e mostre o tanto de dolar que ela consegue comprar.  considere que o dolar = 5
'''
carteira = float(input('quando de dinheiro você tem na carteira? '))
valor_dolar = 3.27

dolares = carteira / valor_dolar

print(f'Com {carteira:.2f} você consegue compra {dolares:.2f} dolares.')