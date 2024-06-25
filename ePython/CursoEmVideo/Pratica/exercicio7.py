'''
Desenvolva um programa que leia as duas notas de um aluno, calcule a sua média e mostre na tela.
'''
nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))

soma = nota1 + nota2
media = soma / 2

print(f'A media da sua nota:{media}')