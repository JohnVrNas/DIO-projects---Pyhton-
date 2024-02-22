import os
os.system('cls')
numa = []
numb = []
for c in range(10):
    numa.append(int(input(f'Digite o {c+1}° número: ')))
for i in numa:
    if i > 15:
        numb.append(i)
print(f'A lista abaixo contém todos os números acima de 15')
print(numb)