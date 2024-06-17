'''
Enquanto a operação for verdadeira ela vai fazer um loop, por exemplo: x =2 + 2 =4, ai volta e faz a mesma operação até chegar  a 10 ou numero aproximado.
'''
x = 2
while(x <= 10):
    print(x)
    x += 2

'''
O Programa ira repetir até digitar um numero maior que zero.
'''
x = int(input("Escreva um numero maior que zero: "))
while (x <= 0):
    x = int(input("Escreva um numero maior que zero: "))
print(f"Você digitou {x}. Encerrando o programa...")

#Interropendo um loop com break(sair ou parar)
print("Digite uma mensagem que ira repetir para você: ")
print("Para encerrar o programa escreva 'sair'. ")
while True:
    texto = input(" ")
    print(texto)
    if texto == "sair":
        break
print("Encerrando programa... ")

#Instrução continue. Serve para voltar o laço ao inicio.

while True:
    nome = input("Login: ")
    if(nome != "vinicios"):
        print("Nome de usuario incorreto.")
        continue # Volta ao inicio se digitar o nome errado

    senha = input("Senha: ")
    if(senha == "123"):
        break  # Encerra o programa
print("Acesso concedido.")

#
for i in range(10,0,-2):
    print(i)