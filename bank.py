menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor incorreto tente novamente.")

    elif opcao == "s":
        valor = float(input("valor do saque: "))

        sem_saldo = valor > saldo

        limitepsaque = valor > limite

        limitediariosaques = numero_saques >= LIMITE_SAQUES

        if sem_saldo:
            print("Você não tem saldo suficiente.")

        elif limitepsaque:
            print("O valor do saque ultrapassa o valor máximo por saque.")

        elif limitediariosaques:
            print("Número de saques excedido limite de saque.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Seleção incorreta tente novamente.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
