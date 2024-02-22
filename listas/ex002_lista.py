import os
os.system('cls')
num = []
for i in range(6):
    num.append(int(input(f'Digite o {i+1}º número: '))) 
    
for i in range (6):
    print(f'{i} => {num[i]}')
    