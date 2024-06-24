'''
Exercício 2
" Crie um jogo de pedra, papel ou tesoura
(Jokenpô). Você deverá jogar contra o
computador. Você irá sempre escolher uma
das opções: 1 - pedra, 2 - papel, 3 - tesoura
" O computador irá sempre sortear
um número de 1 até 3 para jogar
" Armazene todos os resultados em uma
lista e, no final, apresente o vencedor
" Encerre o programa ao digitar zero

'''
import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x<min) or (x > max)):
        x = int(input(pergunta))
    return x 

def vencedor (jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1: #pedra
        if jogador2 == 1: #pedra
            empate += 1
        elif jogador2 == 2: #Papel
            v2 += 1
        elif jogador2  == 3: #tesoura
            v1 += 1
    elif jogador1 == 2: #Papel
        if jogador2 == 1: #pedra
            v1 += 1
        elif jogador2 == 2: #Papel
            empate += 1
        elif jogador2  == 3: #tesoura
            v2 += 1
    elif jogador1 == 3: #Tesoura
        if jogador2 == 1: #pedra
            v2 += 1
        elif jogador2 == 2: #Papel
            v1 += 1
        elif jogador2  == 3: #tesoura
            empate += 1

    resultados = [v1, v2, empate]
    return resultados
#PROGRAMA PRINCIPAL
print('JOKENPO')
print ('1 - Pedra')
print ('2 - Papel')
print ('3 - Tesoura')

jogadas = []
resultados = []
v1 = 0
v2 = 0 
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not j1: 
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

for jogada in jogadas:
    for dado in jogada:
        print(dado, end = ' ')
    print()

print(f'Numero de vitorias do jogador 1: {resultados[0]}')
print(f'Numero de vitorias do jogador 2: {resultados[1]}')
print(f'Numero de empates: {resultados[2]}')