from banco import Banco
import os

b = Banco()
cont = 0

while True:

    print(' sim - para criar uma conta\n não para sair')
    opcao = input('deseja criar um cliente nesse banco: ').strip().lower()
    os.system('cls') or None
    if opcao == 'não' or opcao == 'nao':
        break

    nome = input('qual seu nome: ').strip().lower()
    idade = int(input('qual sua idade: '))
    print(' 1 - conta poupanca\n 2- conta corrente')
    tipo = input('qual tipo de conta: ')
    b.criarUsuarios(nome, idade, tipo)
    os.system('cls') or None
    b.relatorio(nome)

    while True:

        print(' sim - para continuar com opcoes\n não - para sair')
        opcaoConta = input(' deseja ver as opcoes da conta: ').strip().lower()
        os.system('cls') or None
        if opcaoConta == 'não' or opcaoConta == 'nao':
            break

        print(' 1- deposito\n 2 - saque\n 3- alterar limite\n 4 - relatorio conta')
        quefazer = input('insira a opção: ')
        os.system('cls') or None

        if quefazer == '1':
            nome = input('nome titular: ').strip().lower()
            valor = float(input('valor de deposito: '))
            b.deposito(nome, valor)
        elif quefazer == '2':
            nome = input('nome titular: ').strip().lower()
            valor = float(input('valor do saque: '))
            b.sacar(nome, valor)
        elif quefazer == '3':
            nome = input('nome titular: ').strip().lower()
            valor = float(input('valor do novo limite: '))
            b.limiteCC(nome, valor)
        elif quefazer == '4':
            nome = input('nome titular: ').strip().lower()
            b.relatorio(nome)
        else:
            continue