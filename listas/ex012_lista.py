import os
os.system('cls')
print("""6. Faça um programa em Python que leia 15 números 
      inteiros. Determine e mostre quantas vezes o 
      número 0 é repetido na lista.""")
num = []
cont = 0
for i in range (15):
    num.append(int(input(f"Digite o {i+1}º número: ")))
for c in num:
    if c == 0:
        cont += 1
print(f'Apareceram {cont} na lista')

    
    
