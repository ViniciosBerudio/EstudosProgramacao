"""
Escreva um programa que pergunte a
quantidade de km percorridos por um
carro alugado pelo usuário, assim como a
quantidade de dias pelos quais o carro foi
alugado. Calcule o preço a pagar, sabendo
que o carro custa R$ 60 por dia e R$ 0,15
por km rodado
"""
kmPecorrido = float(input("Quantidade de quilômetros pecorrido? "))
quantidadeDias = float(input("Utilizou o carro por quantos dias? "))
res = ((quantidadeDias * 60) + (kmPecorrido * 0.15))
print(f"Valor total a ser pago ficou de: R$ {res:.2f}")