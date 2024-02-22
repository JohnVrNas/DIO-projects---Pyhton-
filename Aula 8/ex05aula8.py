numeros = []
for i in range(20):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
for numero in numeros:
    metade = numero / 2
    print(f"A metade de {numero} é {metade}")