'''
Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta 2m2.
'''
altura = float(input('Qual o tamnho da altura em metros: '))
largura = float(input('Qual tamanho da largura em metros: '))

area = altura * largura
tinta = 2
rs = area / tinta

print(f'Será necessario usar {rs:.2f} de litros de tinta')