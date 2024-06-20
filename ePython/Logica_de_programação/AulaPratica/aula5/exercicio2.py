"""Exercício 2
o

" Suponha que você é um colecionar de jogos
de videogame. Escreva um algoritmo que
permita cadastrar esses jogos informando o
nome e a qual videogame ele pertence

" Para isso, crie um menu de opções contendo:
cadastrar novo item, listar tudo que foi
cadastrado e sair
" Para resolver esse exercício, crie pelo menos
uma função para cada item do menu

" Além disso, armazene todos os dados em
um arquivo de texto que deve ser salvo em
disco e manter os dados cadastrados
"""
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min)or (x > max)):
        x = int(input(pergunta))
    return x
def existeArquivo(nomeArquivo):
    try: 
        a = open(nomeArquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nomeArquivo):
    try: 
        a = open(nomeArquivo, "wt+")
        a.close()
    except:
        print("Erro na criação do arquivo.")
    else:
        print(f"Arquivo {nomeArquivo} Foi criado com sucesso!\n")

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, "at")
    except:
        print("Erro ao abrir o arquivo.")
    else:
        a.write(f"{nomeJogo};{nomeVideogame}\n")
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
    except:
        print("Erro ao ler arquivo.")
    else:
        print(a.read())
    finally:
        a.close()


#Programa principal
arquivo = "games.txt"
if existeArquivo(arquivo):
    print("Arquivo localizado no computador.")
else:
    print("Arquivo inexistente.")
    criarArquivo(arquivo)


while True:
    print("MENU")
    print("1 - Cadastar novo item")
    print("2 - Listar cadastro")
    print("3 - Sair")

    op = valida_int("Escolha a opcção desejada: ", 1, 3)
    if (op == 1): #Novo item
        print("Opção de cadastar novo selecionada...\n")
        nomeJogo = input("Nome do jogo: ")
        nomeVideogame = input("Nome do VideoGame: ")
        cadastrarJogo(arquivo, nomeJogo,  nomeVideogame)
    elif (op == 2): #Listar
        print("Opção de listar selecionada...\n")
        listarArquivo(arquivo)

    elif (op == 3): 
        print("Encerrando o programa.... ")
        break