"""
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre eles.

"""
vari1 = input('Digite algo: ')
print (type(vari1))
print (f'E alfabetico? {vari1.isalpha()}')
print (f'Só tem espaço? {vari1.isspace()}')
print (f'É um numero? {vari1.isnumeric()}')
print (f'É um alfanumerico? {vari1.isalnum()}')
print (f'Está em maiscula? {vari1.isupper()}')
print (f'Está em minuscula? {vari1.islower()}')
print (f'Está  capitalizada? {vari1.istitle()}')