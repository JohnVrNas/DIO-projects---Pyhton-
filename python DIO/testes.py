import os
from time import sleep
os.system('cls')
print('-='*10, 'BANCO', '-='*10)
print('''
    \t\t[d] - Depositar 
    \t\t[s] - Sacar 
    \t\t[e] - Extrato    
    \t\t[q] - Sair    
    ''')
print('-='*24)
saldo = numero_saques = 0
limite  = 500
extrato = ""
LIMITE_SAQUES = 3
cofre = [0]

#laço de repetição infinito
while True:
    
    op = str(input('=> ')).lower()[0]

    if op == 'd':
        valor = float(input('Informe o valor do depósito: R$'))

        #analisando se o valor é compatível ou não 
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            sleep(1)
            print('Depositando...')
            sleep(4)
            print('Depósito feito com sucesso!')

        else:
            print('Valor negativo... Tente novamente')

    elif op == 's':
        valor = float(input('Informe o valor do saque? R$'))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        #variável numero_saques é maior que a LIMITE_SAQUES?
        excedeu_saque = valor > numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação cancelada! Saldo insuficiente... Tente novamente mais tarde.')

        elif excedeu_limite:
            print('Operação cancelada! Valor do saque excede o limite... Tente um valor menor.')

        elif excedeu_saque:
            print('Operação cancelada! Número de saques excedido.')

        elif valor > 0:

            #subtraindo o valor do deposito para o saque
            saldo -= valor
            #registro de extrato para constar no histórico
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print('Operação falhou! O valor informado é inválido.')


    elif op == 'e':
        print('-='*10, 'EXTRATO', '-='*10)
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('-='*27)


    elif op == 'q':

        print('-'*38)
        print('Operação finalizada... Volte Sempre!!')
        print('-'*38)
        break
   

    else:
        print('Opção Inválida... Tente novamente')
