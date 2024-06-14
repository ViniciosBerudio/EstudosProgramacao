'''
Condicional simples
" Traduza as afirmações a seguir para condicionaisem Python

º a) Se idade é maior que 60, escreva: “Você tem
direitos aos benefícios”

º b) Se dano é maior que 10 e escudo é igual a O,
escreva: “Você está morto!”

º c) Se pelo menos uma das variáveis booleanas
norte, sul, leste e oeste resultarem em True,
escreva: “Você escapou!”
'''

direito = 61
if direito > 60:
    print("Você tem direitos aos benefícios")
else:
    pass

dano = 13
escudo = 0
if dano > 10 and escudo == 0:
    print("Você está morto!")
else:
    pass

norte = True
sul = False
leste = False
oeste = False
if (norte == True or sul ==  True or leste == True or oeste == True):
    print("Você escapou!")