import os
os.system('cls')
numa = []
impar = []
for c in range(12):
    numa.append(int(input(f'Digite o {c+1}° número: ')))
for i in range(len(numa)):
    if i % 2 != 0:
        print(f'O número {numa[i]} estava da posição {i}°')
   # print(i, numa[i])

    