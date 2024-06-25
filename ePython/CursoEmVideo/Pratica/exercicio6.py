'''
Crie um algoritmo que leia um numero e  mostre o seu dobro, seu trplo e raiz quadrada.
'''
n = float(input('Digite um numero: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print(f'O dobro de {n} é {dobro}, triplo {triplo} e raiz quadrada {raiz:.2f}')