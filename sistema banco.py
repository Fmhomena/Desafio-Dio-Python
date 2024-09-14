menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        
        else: 
            print("operação falhou! o valor informado é invalido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saques:
            print("operacao falhou! Número maximo de saques excedido")
        
        
        elif excedeu_limite:
            print("operacao falhou! o valor do saque excede o limite.")

        elif excedeu_saques:
            print("operacao falhou! Número maximo de saques excedida.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}/n"
            numero_saques += 1 
        
        else:
            print("operacao falhou! o valor informado é invalido")
    
    elif opcao == "3":
        print("\n=======================Extrato=========================")
        print("não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=============================================")


    elif opcao == "4":
        break

    else:
        print("operacao invalida, por favor selecione novamente a operacao desejada.")

            
            
