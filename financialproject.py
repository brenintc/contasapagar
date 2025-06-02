print()
print("Bem vindo ao sistema de contas a pagar!")
print("Para adicionar uma conta digite 1, se não quiser adicionar mais nenhuma conta digite 2")
print()
contas = []
while True:
    print("1. ADICIONAR CONTA")
    print("2. VER CONTAS")
    print("3. REMOVER CONTA")
    print("4. SAIR DO SISTEMA")

    opcao = input("Opcao: ")

    if opcao == "1":
        nova = input("[Valor, Descrição] Nova conta: R$")
        contas.append(nova)
        print(f"'{nova}' adicionada!")

    elif opcao == "2":
        print("Contas:")
        for i in enumerate(contas, 1):
            print(f"{i}")

    elif opcao == "3":
        if not contas:
            print("Nao há contas para remover...")
            continue
        num = input("Numero da conta a remover: ")
        if num.isdigit() and 0 < int(num) <= len(contas):
            removida = contas.pop(int(num)-1)
            print(f"'{removida}' removida!")
        else:
            print("Numero inválido!")

    elif opcao == "4":
        print("Até logo!")
        break

    else:
        print("Essa opção está indisponível, por favor tente novamente.")