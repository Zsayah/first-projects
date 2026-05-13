while True:
    print("=== Lista de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Remover tarefa")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a tarefa: ")
        with open("tarefa.txt", "a") as arquivo:
            arquivo.write(f"{tarefa}\n")
    elif opcao == '2':
        arquivo = open("tarefa.txt", "r")
        conteudo = arquivo.read()
        print(conteudo)

    elif opcao == '4':
        print('Bye')
        break







