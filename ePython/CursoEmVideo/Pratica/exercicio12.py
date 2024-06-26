'''
Faça um algoritmo que leia o preço do produto e mostre seu novo preço, com 5% de desconto.
'''
preco = float(input('Qual o preço do produto: '))
porcentagem_desconto = 5 

valor = preco - (preco * (porcentagem_desconto / 100))

print(f'O valor com desconto ficou de {valor:.2f}')
