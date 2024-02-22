import os
os.system('cls')
numa = []
cont = 0
for c in range(8):
    numa.append(int(input(f'Digite o {c+1}° número: ')))
for i in numa:
    if i % 3 == 0:
        cont += 1
print(f'Na lista existem {cont} números múltiplos de 3')
