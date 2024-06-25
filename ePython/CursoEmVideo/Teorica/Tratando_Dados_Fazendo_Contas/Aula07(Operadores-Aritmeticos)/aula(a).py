n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero:  '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
# \n para quebra uma linha e 'end' para juntar as linhas
print(f'A soma é {s},\n o produto {m}, e a divisao {d}', end = ', ')
print(f'A divisao inteira {di} e a potencia {p}')