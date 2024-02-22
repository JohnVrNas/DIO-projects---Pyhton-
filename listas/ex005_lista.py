import os
os.system('cls')
num = []
for i in range(5):
    num.append(int(input(f'Digite o {i+1}° número positivo: ')))
for i in range(5):
    if num[i] < 0:
        num[i] = 0
for n in num:
    print(f'Esse foi o número: {n}')