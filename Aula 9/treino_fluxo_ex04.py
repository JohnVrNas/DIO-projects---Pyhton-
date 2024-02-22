import os
os.system('cls')
soma_idade = cont_90 = cont_alto = cont21_30 = 0
for i in range(1,25):
    peso = float(input(f'Digite o {i}° peso em Kg: '))
    while peso < 0.5 or peso > 300:
        print('Peso inválido...Tente novamente')
        peso = float(input(f'Digite o {i}° peso em Kg: '))
    altura = float(input(f'Digite a {i}° altura: '))
    while altura < 0.5 or altura > 3.00:
        print('Altura inválida...Tente novamente')
        altura = float(input(f'Digite a {i}° altura: '))
    idade = int(input(f'Digite a {i}° idade: '))
    while idade < 1 or idade > 120:
        print('Idade inválida...Tente novamente')
        idade = int(input(f'Digite a {i}° idade: '))
    os.system('cls')
    if peso > 90 and altura < 1.60:
        cont_90 +=1 
    if altura > 1.90:
        cont_alto += 1
        if idade >=21 and idade <30:
            cont21_30 +=1
    soma_idade += idade
media_idade = soma_idade/3
if cont_alto > 0:
    percentual = (cont21_30/cont_alto)*100
    print(f'O percentual de pessoas entre 21 e 30 anos que medem mais de 1.9: {percentual}')
else:


    print('Não há pessoas com mais de 1.9 metros')
print(f'A média de idade das pessoas é de {media_idade:.2f}')
print(f'A quantidade de pessoas com mais de 90Kg e abaixo de 1.60 de altura são {cont_90}')