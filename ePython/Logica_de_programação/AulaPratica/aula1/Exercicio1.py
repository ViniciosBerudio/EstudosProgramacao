"""
Desenvolva um algoritmo que solicite
ao usuário o preço de um produto e um
percentual de desconto a ser aplicado a ele.
Calcule e exiba o valor do desconto e o preço
final do produto
"""
preco = float(input ("Preço do produto: "))
percentual = float(input ("Qual o percentual do desconto? "))
desconto = preco * (percentual / 100)
final = preco - desconto
print(f"O preço do produto é {preco} Desconto de {percentual}% ")
print(f"Valor calculado de desconto: {desconto}. Valor final do produto: {final}")