# linha de codigo para mudar o nome da biblioteca(as). para importa(import)
#import math as m

#print(m.sqrt(9))

#para importar uma função somente:
#from math import sqrt
#importando uma função não precisa de decoloca o nome da biblioteca na hora de escrever o codigo:
#print(sqrt(9))

'''
Lista
es " Dada uma lista contendo as
notas de alunos em uma disciplina,
escreva uma expressão para:
notas = [9,7,7,10,3,9,6,6,2]
a) Encontrar quantos alunos tiraram nota 7
b) Alterar a última nota para 4
c) Encontar a maior nota
d) Ordenar a lista de notas
e) A media de notas
'''
#a)
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas.count(7))
#b)
notas[-1] = 4
print (notas)
#c)
print(max(notas))
#d)
notas.sort()
print(notas)
#e)
print(sum(notas) / len(notas))