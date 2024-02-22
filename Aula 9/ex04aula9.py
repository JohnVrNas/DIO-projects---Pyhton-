import os
os.system('cls')
total = preco = 0
resp = 'S'
while resp == 'S':
    os.system('cls')
    print('-='*10, 'LANCHONETE BOM APETITE', '-='*10)
    print('''
    \t\t[100] - Cachorro quente - R$2,50
    \t\t[101] - Bauru simples   - R$2,00
    \t\t[102] - Bauru c/ovo     - R$3,50
    \t\t[103] - Hambúrguer      - R$5,10
    \t\t[104] - Cheeseburguer   - R$3,30
    \t\t[105] - Refrigerante    - R$2,00
    ''')
    print('Para fazer o pedido é só colocar o código do produto')
    pedido = int(input('O que deseja pedir? '))
    while pedido < 100 or pedido > 105:
        pedido = int(input('Opção inválida... Digite um número entre 100 e 105: '))
    qnt = int(input('Quantidade do produto desejado: '))
    while qnt < 1:
        qnt = int(input('Opção Inválida... Digite novamente a quantidade desejada: '))
    if pedido == 100:
        preco = 2.50
    elif pedido == 101:
        preco = 2.00
    elif pedido == 102:
        preco = 3.50
    elif pedido == 103:
        preco = 5.10
    elif pedido == 104:
        preco = 3.30
    else:
        preco = 2.00
    total += preco*qnt
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
os.system('cls')
print('~'*35)
print(f'O total da compra foi de R${total:.2f}')
print('~'*35)