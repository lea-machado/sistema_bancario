from time import sleep

print("Sistema bancário")

menu="""
-------------MENU-------------
1- Depósito
2- Saque
3- Extrato
4- Criar usuário
5- Criar conta corrente
6- Informações do usuário
7- Sair
------------------------------"""

def funcao_deposito(saldo, deposito, extrato, /):
    if deposito>0:
        saldo += deposito
        extrato.append(f"+ R$ {deposito:.2f}")
        print("Valor depositado com sucesso!")
    else:
        print("Valor inválido.")

    return saldo

def funcao_saque(*, quantidade_saques_diario, saldo, extrato):
    if quantidade_saques_diario<3:
        saque = float(input("\nDigite o valor a ser sacado: "))
        if saque>saldo:
            print("\nSaldo insuficiente para realizar o saque!")
        elif saque>500:
            print("\nValor acima do limite de R$500,00 por saque!")
        elif saque>0:
            saldo -= saque
            quantidade_saques_diario += 1
            extrato.append(f"- R$ {saque:.2f}")
            print("Valor sacado com sucesso!")
        else:
            print("Valor inválido.")
    else:
        print("\nVocê já realizou o número máximo de saques diários por hoje!")

    return saldo, quantidade_saques_diario

def funcao_extrato(saldo, /, *, extrato):
    if len(extrato)==0:
        print("\nAinda não foram realizadas movimentações!")
    else:
        print("\n-------Extrato-------")
        for operacao in extrato:
            print(operacao)
        print("-------------------")
        print(f"Saldo: R$ {saldo:.2f}")

def funcao_criar_usuario(dados_clientes, lista_clientes):
    cpf, posicao_cliente = buscar_cpf(lista_clientes)
    if posicao_cliente > -1:
        print("Este CPF já está cadastrado")
    else:
        informacoes_usuario(cpf, dados_clientes, lista_clientes)
        print("Usuário cadastrado com sucesso!")

def buscar_cpf(lista_clientes):
    posicao_cliente = -1
    cpf = input("Informe o número do CPF (somente números): ")
    tamanho_lista = len(lista_clientes)
    for i in range(tamanho_lista):
        if cpf == lista_clientes[i][2]:
            posicao_cliente = i

    return cpf, posicao_cliente
        
def informacoes_usuario(cpf, dados_clientes, lista_clientes):
    dados_clientes.append(input("Digite o seu nome: "))
    dados_clientes.append(input("Digite a sua data de nascimento: "))
    dados_clientes.append(cpf)
    logradouro = input("Logradouro: ")
    numero_residencia = int(input("Número: "))
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    sigla_estado = input("Sigla do estado: ").upper()
    endereco = f"{logradouro}, {numero_residencia} - {bairro} - {cidade}/{sigla_estado}"
    dados_clientes.append(endereco)
    lista_clientes.append(dados_clientes[:])
    dados_clientes.clear()

def funcao_criar_conta(numero_conta, conta_individual, contas, lista_clientes, AGENCIA):
    print("Criar conta")
    posicao_cliente = -1
    cpf = input("Informe o número do CPF (somente números): ")
    tamanho_lista = len(lista_clientes)
    for i in range(tamanho_lista):
        if cpf == lista_clientes[i][2]:
            posicao_cliente = i
    if posicao_cliente==-1:
        print("Cadastro de usuário não encontrado para este CPF!")
    else:
        conta_individual.append(AGENCIA)
        conta_individual.append(numero_conta)
        conta_individual.append(lista_clientes[posicao_cliente][0])
        conta_individual.append(lista_clientes[posicao_cliente][2])
        contas.append(conta_individual[:])
        conta_individual.clear()
        print("Conta criada com sucesso!")

    return contas

def informacoes_do_usuario(lista_clientes, contas):
    cpf, posicao_cliente = buscar_cpf(lista_clientes)
    if posicao_cliente == -1:
        print("Cadastro de usuário não encontrado para este CPF!")
    else:
        print(estrutura_dados_usuario(lista_clientes, posicao_cliente))
        if buscar_contas(contas, cpf)==False:
            print("Ainda não abertas contas para este usuário.")

def buscar_contas(contas, cpf):
    tamanho_lista = len(contas)
    for i in range(tamanho_lista):
        if cpf == contas[i][3]:
            print(f"\nAgência: {contas[i][0]} \tNúmero da conta: {contas[i][1]}")

def estrutura_dados_usuario(lista_clientes, posicao_cliente):
    estrutura_dados_usuario = f"""\n
    -------INFORMAÇÕES USUÁRIO-------
    Nome: {lista_clientes[posicao_cliente][0]}
    Data de nascimento: {lista_clientes[posicao_cliente][1]}
    CPF: {lista_clientes[posicao_cliente][2]}
    Endereço: {lista_clientes[posicao_cliente][3]}"""

    return estrutura_dados_usuario

def main():
    saldo = 0
    quantidade_saques_diario = 0
    AGENCIA = "0001"
    extrato = []
    lista_clientes = []
    dados_clientes = []
    contas = []
    conta_individual = []

    while True:
        sleep(0.45)
        print(menu)
        opcao = int(input("Digite a opção desejada: "))
        while opcao<1 or opcao>7:
            opcao = int(input("Opção inválida, digite novamente:"))
        if opcao==1:
            deposito = float(input("\nDigite o valor a ser depositado: "))
            saldo = funcao_deposito(saldo, deposito, extrato)
        if opcao==2:
            saldo, quantidade_saques_diario = funcao_saque(
                quantidade_saques_diario = quantidade_saques_diario,
                saldo = saldo, extrato = extrato)
        if opcao==3:
            funcao_extrato(saldo, extrato=extrato)
            sleep(0.20)
        if opcao==4:
            funcao_criar_usuario(dados_clientes, lista_clientes)
        if opcao==5:
            numero_conta = len(contas) + 1
            funcao_criar_conta(numero_conta, conta_individual, contas, lista_clientes, AGENCIA)
        if opcao==6:
            informacoes_do_usuario(lista_clientes,contas)
        if opcao==7:
            break

main()