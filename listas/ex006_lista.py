import os
os.system('cls')
print('1. Elabore um programa em Python que receba uma lista com 10 números reais e imprima os números maiores do que 15.')
numa = []
numb = []
for c in range(15):
    numa.append(int(input(f'Digite o {c+1}° número: ')))
maior = int(input('Digite o maior número: '))
for i in numa:
    if i > maior:
        numb.append(i)
print(f'A lista abaixo contém todos os números acima de {maior}')
print(numb)