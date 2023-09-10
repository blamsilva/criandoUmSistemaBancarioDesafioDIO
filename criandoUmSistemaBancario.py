# Variáveis
saldo = 1000.00
limite = 500.00
qsaque = 3
opcao = 0
extrato = [saldo]
marcacao = "-" * 14


while True:

    opcao = int(input("Digite a opção Desejada:\n1 - Saldo\n2 - Depósito\n3 - Saque\n4 - Extrato\n0 - Sair\n:"))
    print(marcacao)
    if opcao == 1:
        print(f"{'SALDO' : ^14}")
        print(marcacao)
        print(f"R$ {saldo:>10.2f}")
    elif opcao == 2:
        print(f"{'DEPÓSITO' : ^14}")
        print(marcacao)
        deposito = float(input("Digite o valor a ser depositado:\nR$ "))
        saldo += deposito
        extrato.append(deposito)
    elif opcao == 3:
        if qsaque > 0:
            print(f"{'SAQUE' : ^14}")
            print(marcacao)
            saque = float(input("Qual o valor do Saque:\nR$  "))
            if saque > saldo:
                print("Não existe saldo suficiente para operação")
            elif saque > 500:
                print("Valor de saque superior ao permitido!")
            else:
                saldo -= saque
                qsaque -= 1
                extrato.append(-saque)
        else:
            print("Limite de quantidade de saques já Realizado.\nSaque não permitido! ")
    elif opcao == 4:
        print(f"{'EXTRATO' : ^14}")
        print(marcacao)
        for i in extrato:
            print(f"R$ {i:>10.2f}")
        print(f"{marcacao}\nR$ {saldo:>10.2f} - Saldo ")
    elif opcao == 0:
        break
    else:
        print("Opção Inválida, por favor selecione novamente uma opção válida.")
    print(marcacao)
print("Conta Deslogada, Obrigado e Volte Sempre!")
