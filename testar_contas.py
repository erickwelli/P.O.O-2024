from conta_bancaria import Conta_bancaria
from conta_corrente import Conta_corrente
from conta_poupanca import Conta_poupanca

conta_poupanca = 0
conta_corrente = 0
opcao = 0
while opcao != 8:
    print("*** Sistema de Gestão de Contas Bancárias ***")
    print("1) Cadastrar nova conta")
    print("2) Exibir conta")
    print("3) Depositar")
    print("4) Sacar")
    print("5) Verificar saldo")
    print("6) Verificar rendimento (Conta Poupança)")
    print("7) Aplicar rendimento (Conta Poupança)")
    print("8) SAIR")

    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        tipo = int(input("Informe o tipo de conta: 1) Conta Corrente  2) Conta Poupança: "))
        nome = input("Informe o nome do titular: ")
        cpf = input("Informe o CPF do titular: ")
        saldo = float(input("Informe o saldo inicial: "))

        if tipo == 1:
            numerocc = input("Informe o número da conta corrente: ")
            conta_corrente = Conta_corrente(nome, cpf, saldo, numerocc)
            print("Conta Corrente criada com sucesso!")
        elif tipo == 2:
            rendimento = float(input("Informe a taxa de rendimento (por exemplo, 0.005 para 0.5%): "))
            conta_poupanca = Conta_poupanca(nome, cpf, saldo, rendimento)
            print("Conta Poupança criada com sucesso!")
        else:
            print("Tipo de conta inválido.")

    if opcao == 2:
        tipo = int(input("Exibir qual conta: 1) Conta Corrente  2) Conta Poupança: "))

        if tipo == 1:
            if conta_corrente:
                print(conta_corrente.mostrarcc())
            else:
                print("Conta Corrente não encontrada.")
        elif tipo == 2:
            if conta_poupanca:
                print(conta_poupanca.mostrar_conta())
            else:
                print("Conta Poupança não encontrada.")
        else:
            print("Tipo de conta inválido.")

    if opcao == 3:
        tipo = int(input("Depositar em qual conta: 1) Conta Corrente  2) Conta Poupança: "))
        valor = float(input("Informe o valor a ser depositado: R$ "))

        if tipo == 1:
            if conta_corrente:
                print(conta_corrente.depositar(valor))
            else:
                print("Conta Corrente não encontrada.")
        elif tipo == 2:
            if conta_poupanca:
                print(conta_poupanca.depositar(valor))
            else:
                print("Conta Poupança não encontrada.")
        else:
            print("Tipo de conta inválido.")

    if opcao == 4:
        tipo = int(input("Sacar de qual conta: 1) Conta Corrente  2) Conta Poupança: "))
        valor = float(input("Informe o valor a ser sacado: R$ "))

        if tipo == 1:
            if conta_corrente:
                print(conta_corrente.sacar(valor))
            else:
                print("Conta Corrente não encontrada.")
        elif tipo == 2:
            if conta_poupanca:
                print(conta_poupanca.sacar(valor))
            else:
                print("Conta Poupança não encontrada.")
        else:
            print("Tipo de conta inválido.")

    if opcao == 5:
        tipo = int(input("Verificar saldo de qual conta: 1) Conta Corrente  2) Conta Poupança: "))

        if tipo == 1:
            if conta_corrente:
                print(conta_corrente.verificar_saldo())
            else:
                print("Conta Corrente não encontrada.")
        elif tipo == 2:
            if conta_poupanca:
                print(conta_poupanca.verificar_saldo())
            else:
                print("Conta Poupança não encontrada.")
        else:
            print("Tipo de conta inválido.")

    if opcao == 6:
        if conta_poupanca:
            print(conta_poupanca.ver_rendimento())
        else:
            print("Conta Poupança não encontrada.")

    if opcao == 7:
        if conta_poupanca:
            print(conta_poupanca.render())
        else:
            print("Conta Poupança não encontrada.")

print("Saindo do sistema...")