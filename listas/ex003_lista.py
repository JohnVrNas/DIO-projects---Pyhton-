import os
os.system('cls')
print('Média de números')
num = []
for c in range(4):
    num.append(int(input(f'Digite o {c+1}° números: ')))
soma = (sum(num))/4
print(f'A média dos números é de {soma:.2f}')