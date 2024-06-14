'''
Expressões booleanas
' Escreva as seguintes expressões booleanas
em linguagem Python
 a) O somatório de 2 com 2 é menor que 4
 b) O valor 7 //3 é igual a 1+1
 c) A soma de 3 elevado ao quadrado com 4
elevado ao quadrado é igual a 25
 d) A soma de 2, 4 e 6 é maior que 12
'''
if (2 + 2 < 4):
    print("Verdadeiro!")
elif (7 // 3 == 1 + 1):
    print("verdadeiro!")
elif (3**2 + 4**2 == 25):
    print("Verdadeiro!")
if (2+4+6 > 12):
    print("Verdadeiro!")

'''
" Escreva as seguintes expressões booleanas
em linguagem Python
º a) 1387 é divisível por 19
º b) 31 é par
º c) O menor valor entre: 34, 29 e 31 é menor
que 30

'''

if(1387 % 19 == 0):
    print("Verdadeiro!")
if(31 % 2 == 0):
    print("Verdadeiro!")
if(min (34, 29,31) < 30):
    print("Verdadeiro!")