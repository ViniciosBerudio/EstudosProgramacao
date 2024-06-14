'''
Condicional composta
" Traduza as afirmações a seguir para condicionais
em Python

º a) Se ano é divisível por 4, escreva: “Pode ser
um ano bissexto”. Caso contrário, escreva:
“Definitivamente não é um ano bissexto”

º b) Se ambas as variáveis booleanas cima e
baixo forem True, escreva: “Decida-se!”, caso
contrário, escreva: “Você escolheu um
caminho!”

'''
ano = 1993
if (ano % 4 == 0):
    print("Pode ser um ano bissexto")
else:
    print("Definitivamente não é  um ano bissexto")

cima = True
baixo = True
if (cima == True and baixo == True):
    print("decida-se!")
else:
    print("Você escolheu um caiminho!")