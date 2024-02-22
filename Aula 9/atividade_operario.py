# JOÃO VICTOR RODRIGUES DO NASCIMENTO - ADS - 11232101507
import os
from time import sleep
os.system('cls')
# Variáveis definidas
tot_folha = tot_pecas = media_mas = media_fem = cont_mas = cont_fem = salario_maior = cont = 0
sm = 724.00
print('\t\t\tMENU PARA TRABALHADORES')

# Loop para informmações de cada operário
for i in range(1, 4):
    numero_operario = int(input(f'{i}º - Digite seu número de operário: '))
    while numero_operario < 1:
        print('Número inválido...Tente novamente com um número real ')
        numero_operario = int(input('Digite seu número de operário: '))
    pecas_operario = int(input(f'{i}º - Digite quantas peças você fez esse mês: '))
    while pecas_operario < 1:
        print('Número inválido...Tente novamente com um número real ')
        pecas_operario = int(input('Digite quantas peças você fez esse mês: '))
    sexo_operario = str(input(f'{i}º - Digite seu sexo [M/F]: ')).upper().strip()[0]
    while sexo_operario not in 'MF':
        print('Opção Inválida... Tente novamente')
        sexo_operario = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

    # Cálculo do salário
    if pecas_operario <= 30:
        salario_operario = sm
    else:
        if pecas_operario > 30 and pecas_operario <= 35:
            salario_operario = sm + (pecas_operario-30) * (sm * 0.03)
        else:
            salario_operario = sm + (pecas_operario-30) * (sm * 0.05)

    # Aualização das variáveis definidas como 0
    print('-'*70)
    print(f'O salário a ser recebido pelo operário de número {numero_operario}º será de R${salario_operario:.2f}')
    print('-'*70)
    tot_folha += salario_operario
    tot_pecas += pecas_operario
    if sexo_operario == 'M':
        media_mas += pecas_operario
        cont_mas += 1
    else:
        media_fem += pecas_operario
        cont_fem += 1
    if cont == 1:
        salario_maior = salario_operario
        num_maior = numero_operario
    else:
        if salario_operario > salario_maior:
            salario_maior = salario_operario
            num_maior = numero_operario

# Cálculo das médias
if cont_mas == 0:
    media_mas = 0
else:
    media_mas = media_mas/cont_mas
if cont_fem == 0:
    media_fem = 0
else:
    media_fem = media_fem/cont_fem
sleep(5)
os.system('cls')
#Saída de dados
print(f'Total da folha de pagamento da fábrica: R${tot_folha:.2f}')
print(f'A fábrica produziu o total de {tot_pecas} peças')
print(f'A média de peças fabricadas pelos homens: {media_mas}')
print(f'A média de peças fabricadas pelas mulheres: {media_mas}')
print(f'O maior salário da fábrica foi do operário ou operária {num_maior}º')
print('-='*15)
print('Obrigado por usar nosso sistema!!')