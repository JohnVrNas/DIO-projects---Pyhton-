import os
os.system("cls") 

salario_minimo = 724 

folha_de_pagamento = 0
total_pecas_fabricadas = 0
total_pecas_homens = 0
total_pecas_mulheres = 0
maior_salario = 0
numero_maior_salario = 0

for i in range(1, 4):
    print(f"Operário {i}ª:")
    numero_operario = int(input("Número do operário: "))
    pecas_fabricadas = int(input("Número de peças fabricadas no mês: "))
    sexo = input("Sexo do funcionário (M/F): ").upper()

    if pecas_fabricadas <= 30:
        classe = 1
        salario = salario_minimo
    elif pecas_fabricadas <= 35:
        classe = 2
        salario = salario_minimo + 0.03 * salario_minimo * (pecas_fabricadas - 30)
    else:
        classe = 3
        salario = salario_minimo + 0.05 * salario_minimo * (pecas_fabricadas - 30)
    folha_de_pagamento += salario
    total_pecas_fabricadas += pecas_fabricadas

    if sexo == "M":
        total_pecas_homens += pecas_fabricadas
    elif sexo == "F":
        total_pecas_mulheres += pecas_fabricadas

    if salario > maior_salario:
        maior_salario = salario
        numero_maior_salario = numero_operario

    print(f"Salário do operário {numero_operario}: R${salario:.2f}")

media_pecas_homens = total_pecas_homens / numero_operario
media_pecas_mulheres = total_pecas_mulheres / numero_operario

# Resultados finais
print(f"Total da folha de pagamento: R${folha_de_pagamento:.2f}")
print(f"Número total de peças fabricadas no mês: {total_pecas_fabricadas}")
print(f"Média de peças fabricadas pelos homens: {media_pecas_homens:.2f}")
print(f"Média de peças fabricadas pelas mulheres: {media_pecas_mulheres:.2f}")
print(f"Operário de maior salário: Operário {numero_maior_salario}")
