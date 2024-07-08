#Mensagem com meu nome
print('[Bem-vindo a empresa do Vinicios Berudio de Oliveira]')

#variavel com meu RU e a lista dos funcionarios cadastrado
id_global = 4677341
lista_funcionarios = []

#classe funcionario


#funcao para cadastra os funcionarios
def cadastrar_funcionario(id):

    global id_global
    id = id_global + 1
    print(f'ID  do funcionario: {id}')
    nome = input('Digite o nome do funcionario: ')
    setor = input('Digite o setor do funcionario: ')
    salario = float(input('Digite o salario do funcionario: '))

#dicionario
    funcionario_dict = {
        'id' : id,
        'nome' : nome,
        'setor' : setor,
        'salario' : salario
    }
    lista_funcionarios.append(funcionario_dict.copy())
    id_global += 1

    print(f'Funcionario {nome} cadastrado com sucesso!')

#função para consultar funcionarios
def consultar_funcionarios():
    while True:
        #Menu de consulta de funcionarios
        print("\nMenu Consultar Funcionários:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")

        opcao = input('Escolha uma opcão entre (1, 2, 3, 4)')

        if opcao == '1':
            print('Funcionario cadastrados: ')
            for funcionario in lista_funcionarios:
                print(f'ID: {funcionario['id']}, nome: {funcionario['nome']}, setor: {funcionario['setor']}, salario {funcionario['salario']}')

        elif opcao == '2':
            id_consulta = int(input('Digite o ID do funcionario: '))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    encontrado = True
                    print('Funcionario encontrado:')
                    print(f'ID: {funcionario['id']}, nome: {funcionario['nome']}, setor: {funcionario['setor']}, salario {funcionario['salario']}')
                    break
            if not encontrado:
                print('Funcionario não encontrado.')

        elif opcao == '3':
            setor_consulta = input('Digite o setor do funcionario:')
            encontrado = False
            print(f'funcionario do Setor {setor_consulta}:')
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == setor_consulta:
                    encontrado = True
                    print(f'ID: {funcionario['id']}, nome: {funcionario['nome']}, setor: {funcionario['setor']}, salario {funcionario['salario']}')
            if not encontrado:
                print(f'Nenhum funcionario encontrado no setor{setor_consulta}.')

        elif opcao == '4':
            print('Retornando ao menu principal...')
            return
        else:
            print('Opção invalida.')

#funcao para remover funcionarios
def remover_funcionario():
    id_remover = int(input('Digite o id do funcionario que vai ser removido: '))
    removido = False
    for funcionario in lista_funcionarios:
        if funcionario['id'] == id_remover:
            removido = True
            lista_funcionarios.remove(funcionario)
            print(f'Funcionario com o id {id_remover} foi removido.')
            break
    if not removido:
        print(f'Funcionario  com o id {id_remover} não foi encontrado.')

#Menu principal do programa
while True:
    print("\nEscolha a opção desejada:")
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Funcionário")
    print("3 - Remover Funcionário")
    print("4 - Sair")

    opcao_principal = input("Digite sua opção (1/2/3/4): ")

    if opcao_principal == '1':
        cadastrar_funcionario(id_global)
        
    elif opcao_principal == '2':
        consultar_funcionarios()

    elif opcao_principal == '3':
        remover_funcionario()

    elif opcao_principal == '4':
        print("Encerrando o programa...")
        break

    else:
        print('Opção invalida. Escolha uma opção entre (1 a 4)')