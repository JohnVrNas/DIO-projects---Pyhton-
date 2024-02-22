import os
os.system('cls')
print('\t\t\tVALOR DE TRANSPORTE')
preco_unitario = int(input('Digite o valor do produto: R$'))
while preco_unitario < 1:
    print('Valor inválido... Tente novamente')
    preco_unitario = int(input('Digite o valor do produto: R$'))
print('''     PAÍS DE ORIGEM
      1  -  EUA
      2  -  MÉXICO
      3  -  OUTROS''')
pais_origem = int(input('Digite o código de país de origem: '))
while pais_origem < 1 or pais_origem > 3:
    print('Código de país inválido... Tente novamente')
    pais_origem = int(input('Digite o código de país de origem: '))
print('''     TRANSPORTE
      T  -  Terrestre
      F  -  Fluvial
      A  -  Aéreo
      ''')
meio_transporte = str(input('Digite o meio de transporte desejado: ')).strip().upper()[0]
while meio_transporte not in 'TFA':
    print('Meio de transporte inválido... Tente novamente')
    meio_transporte = str(input('Digite o meio de transporte desejado: '))
perigo = str(input('A carga a ser entregue é perigosa? [S/N]: ')).upper().strip()[0]
while perigo not in 'SN':
    print('ERRO... Digite novamente')
    perigo = str(input('A carga a ser entregue é perigosa? [S/N]: ')).upper().strip()[0]
if preco_unitario <= 100:
    imposto = (preco_unitario*5)/100
else:
    imposto = (preco_unitario*10)/100
if perigo == 'S':
    if pais_origem == 1:
        valor_transporte = 50
    else:
        if pais_origem == 2:
            valor_transporte = 35
        elif pais_origem == 3:
            valor_transporte = 24
else:
    if pais_origem == 1:
        valor_transporte = 12
    elif pais_origem == 2:
        valor_transporte = 35
    elif pais_origem == 3:
        valor_transporte = 60
frete = valor_transporte + imposto
os.system('cls')
print(f'O valor do imposto a pagar pelo produto é de R${imposto}')
print(f'O valor do transporte do produto ficou R${valor_transporte}')
print(f'O valor total do frete é de R${frete}')