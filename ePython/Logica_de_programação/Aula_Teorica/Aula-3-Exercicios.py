#Le os dois valores inteiro e compara ambos
n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite um segundo valor inteiro: "))
if (n1 > n2):
    print("O primeiro valor é maior que o segundo!")
else:
    print("O segundo valor é menor que o primeiro")

# Desenvolva um programa que leia um valor inteiro e se ele [e par ou ímpar
Valor= int(input("Digite um valor inteiro: "))
#  Se o resto da divis'ao for 0 = par se nao  é impar (% para calcular resto)
if (Valor % 2 ==0):
    print("O numero é par!")
else:
    print("Numero é impar!")

'''
Escreva um algoritmo em que o usuário escolhe se quer comprar maças, laranjas ou bananas. Deverá ser apresentado na tela com as opções: 1 para maça 2 para laranja e 3 para banana.
'''

print("Qual fruta ira comprar?")
print("1 - maças")
print("2 - Laranjas")
print("3 - bananas")
escolha= int(input("Digite o numero de sua escolha: "))
qnt = int(input("Qual a quantidade desejada :"))
if (escolha == 1):
    pagar = qnt * 2.3
    print(f"Você compro {qnt} Maças. total a pagar: {pagar:.4}")
else:
    if (escolha == 2):
        pagar = qnt * 3.6
        print(f"Você compro {qnt} Laranjas. total a pagar: {pagar:.4}")
    else:
        if (escolha == 3):
            pagar = qnt * 1.85
            print(f"Você compro {qnt} bananas. total a pagar: {pagar:.4}")
        else:
            print("Produto inexistente!")

'''
Escreva um algoritmo que leia um nome e idade
    Caso o nome digitado seja Vinicios, escreva isso na tela
    Caso o usuario qualquer outro nome verifique sua idade. Se for menor que 18 anos, informe que é de menor. Se for maior que 100 anos iforme que esta pessoa não existe.
'''
nome = input("Escreva o nome: ")
idade = int(input("Digite sua idade: "))
if (nome == "Vinicios"):
    print("Olá, Vinicios!")
elif idade < 18:
    print("Você não é Vinicios e você é menor de idade.")
elif idade > 100:
    print("Essa pessoa não existe.")
else:
    print(f"Oi, {nome} a sua idade é {idade}")