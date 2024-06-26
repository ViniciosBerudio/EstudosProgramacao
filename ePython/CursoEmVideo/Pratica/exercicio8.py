'''
Escreva um programa que leia o valor em metros e o exiba em centimetros e milimitros.
'''
metro = float(input('Digite o valor em metros: '))

centimetro = metro * 100
milimetro = metro * 1000

print(f'====== Conversão de medidas ======')
print(f'Valor em metros: {metro} m')
print(f'Valor em centimetros: {centimetro} cm')
print(f'Valor em milimetros: {milimetro} mm')