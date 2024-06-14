'''
Exercício 1

" Faça um algoritmo que receba três valores,
representando os lados de um triângulo
fornecidos pelo usuário. Verifique se os
valores formam um triângulo e classifique
como
º a) Equilátero (três lados iguais)
º b) Isósceles (dois lados iguais)
º c) Escaleno (três lados diferentes)
'''
A = int(input("Digite o primeiro lado do triangulo: "))
B = int(input("Digite o segundo lado do triangulo: "))
C = int(input("Digite o terceiro lado do triangulo: "))

if ((A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A)):
#Se chegou até aqui é pq o triangulo é valido!
    if (A != B and  A != C and B != C):
        print("Escanelo!")
    else:
        if(A == B and B == C):
            print("Equilatero")
        else:
            print("Isosceles")
else:
    print("Ao menos um dos valores indicados não servem para forma um triangulo!")