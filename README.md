# DIO | Desafio de projeto: Sistema bancário

Projeto realizado para resolver a proposição de desafio do [Bootcamp Potência Tech powered by iFood | Ciência de Dados](https://web.dio.me/track/potencia-tech-powered-ifood-ciencias-de-dados-com-python) na plataforma DIO.

## Desafio 1: Criando um sistema bancário com Python.
### Objetivo geral:
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
### Operação de depósito
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
### Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
### Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem, deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações.".
Os valores devem ser exibidos utilizando o formato R$ XXX.XX.

## Desafio 2: Otimizando o sistema bancário com funções Python.
### Objetivo geral:
Separar as operações existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.
### Função de depósito
A função depósito deve receber os argumentos apenas por posição (positional only).
### Função de saque
A função de saque deve receber os argumentos apenas por nome (keyword only).
### Função de extrato
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo. Argumentos nomeados: extrato.
### Função criar usuário (cliente)
O programa deve armazenar os usuários em uma lista. Um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma string com formato: logradouro, número - bairro - cidade/sigla estado. Devem ser armazenados somente os números do CPF. Não podemos cadastrar dois usuários com o mesmo CPF.
### Função criar conta corrente
O programa deve armazenar contas em uma lista. Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.