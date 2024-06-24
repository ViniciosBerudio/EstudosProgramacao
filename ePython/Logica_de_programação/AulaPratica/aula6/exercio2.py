'''
" Escreva um algoritmo que crie uma
tupla com 5 palavras. Encontre dentro
dessa tupla as vogais de cada palavra.
Faça um print na tela com o nome da
palavra e suas respectivas vogais

'''
palavras = ('mario', 'Luigi', 'Link', 'Peach', 'Yoshi')

for palavra in palavras: 
    print(f'\nPalavra: {palavra.upper()}. Vogais:')
    for Letra in palavra:
        if Letra.lower() in 'aeiou':
            print(Letra.upper(), end = ' ')