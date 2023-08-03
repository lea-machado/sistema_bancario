from time import sleep

print("Sistema bancário")

menu="""
-------------MENU-------------
1- Depósito
2- Saque
3- Extrato
4- Sair
------------------------------"""
saldo = 1000
quantidade_saques_diario = 0
extrato = []

while True:
    sleep(0.45)
    print(menu)
    opcao = int(input("Digite a opção desejada: "))
    while opcao<1 or opcao>4:
        opcao = int(input("Opção inválida, digite novamente:"))
    if opcao==1:
        deposito = float(input("\nDigite o valor a ser depositado: "))
        saldo += deposito
        extrato.append(f"+ R$ {deposito:.2f}")
        print("Valor depositado com sucesso!")
    if opcao==2:
        if quantidade_saques_diario<3:
            saque = float(input("\nDigite o valor a ser sacado: "))
            if saque>saldo:
                print("\nSaldo insuficiente para realizar o saque!")
            elif saque>500:
                print("\nValor acima do limite de R$500,00 por saque!")
            else:
                saldo -= saque
                quantidade_saques_diario += 1
                extrato.append(f"- R$ {saque:.2f}")
                print("Valor sacado com sucesso!")
        else:
            print("\nVocê já realizou o número máximo de saques diários por hoje!")
    if opcao==3:
        if len(extrato)==0:
            print("\nAinda não foram realizadas movimentações!")
        else:
            print("\n-------Extrato-------")
            for operacao in extrato:
                print(operacao)
            print("-------------------")
            print(f"Saldo: R$ {saldo:.2f}")
        sleep(0.20)
    if opcao==4:
        break
