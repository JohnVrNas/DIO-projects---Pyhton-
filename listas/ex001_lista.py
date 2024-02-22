numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
m234 = []
print('Intervalo de 1 a 9:',numeros[1:10]) #A
print('Intervalo de 8 a 13:',numeros[8:14]) #B
print('Números pares:', numeros[0::2]) #C
print('Números ímpares:',numeros[1::2]) #D
for valor in numeros:
    if valor % 2 == 0 and valor % 3 == 0 and valor % 4 == 0:
        m234.append(valor)
print('Múltiplos de 2, 3 e 4:',m234) #E
lista_reversa = numeros
lista_reversa.sort(reverse=True)
print('Lista reversa:',lista_reversa) #F
lista_reversa.sort(reverse=False)
soma = sum(numeros[10:16]) #G
print(soma)
novo = numeros
numeros.append(69)
print('Lista com novos elementos:',numeros) #H
del numeros[6]
numeros.insert(6, 'Delício')
print('Substituir o elemento com índice 6:',numeros)