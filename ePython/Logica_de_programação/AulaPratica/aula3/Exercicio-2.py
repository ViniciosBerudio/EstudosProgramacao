'''
Exercício 2

" Escreva um algoritmo que leia dois valores
numéricos e que pergunte ao usuário qual
operação ele deseja realizar: adição (+),
subtração (-), multiplicação (*) ou divisão
(/). Exiba na tela o resultado da operação
desejada (exercício da apostila - aula 3)
'''
print("CALCULADORA")
print("+ Adicao")
print("- subtracao")
print("* multiplicacao")
print("/ divisao")
print("pressione qualquer tecla para sair.")

op = input("Qual operacao deseja realizar? ")
x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))

if (op == "+"):
    res = x + y
    print(f"Resultado: {res}")
elif (op == "-"):
    res = x - y
    print(f"Resultado: {res}")
elif (op == "*"):
    res = x * y
    print(f"Resultado: {res}")
elif (op == "/"):
    res = x / y
    print(f"Resultado: {res}")
else:
    print("Encerrando o programa...")