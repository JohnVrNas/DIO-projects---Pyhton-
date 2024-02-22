import os
os.system('cls')
numa = []
numb = []
for c in range(9):
    numa.append(int(input(f'Digite o {c+1}° número: ')))
for i in numa:
    if i % 2 == 0:
        numb.append(i)
soma = sum(numb)
print(f'A soma de todos os números pares dessa lista é de: {soma}')
