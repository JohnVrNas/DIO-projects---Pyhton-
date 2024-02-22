import os
os.system('cls')
cont_apro = cont_repro = 0
print('Reprovado ou Aprovado')
for i in range(1, 10+1):
    peca = str(input(f'Digite o estado da {i}° peça: ')).upper().strip()[0]
    if peca == 'A':
        cont_apro += 1
    else:
        cont_repro += 1
print(f'''Ao todo tivemos:
{cont_apro} Aprovadas
{cont_repro } Reprovadas''')
