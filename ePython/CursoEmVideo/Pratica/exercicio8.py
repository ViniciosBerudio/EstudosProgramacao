'''
Escreva um programa que leia o valor em metros e o exiba em centimetros e milimitros.
'''
metro = float(input('Digite o valor em metros: '))

cm = metro * 100
mm = metro * 1000

print(f'====== Conversão de medidas ======')
print(f'Valor em metros: {metro} m')
print(f'Valor em centimetros: {cm} cm')
print(f'Valor em milimetros: {mm} mm')