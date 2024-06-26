'''
Faça um algoritmo que leia o salario do funcionario e mostre seu novo saalario com aumento de 15%.
'''
salario = float(input('Qual seu salario atual: '))

porcentagem = 15 
salario_novo = salario + (salario * (porcentagem / 100))

print(f'Seu salario novo sera {salario_novo:.2f}')