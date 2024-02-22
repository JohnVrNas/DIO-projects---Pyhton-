import os
os.system('cls')
pais_a = 98000000
pais_b = 200000000
taxa_crescimento_a = 0.035
taxa_crescimento_b = 0.015
anos = 0
while pais_a < pais_b:
    pais_a = pais_a * (1 + taxa_crescimento_a)
    pais_b = pais_b * (1 + taxa_crescimento_b)
    anos += 1
print(f'Depois de {anos} anos o país A conseguiu se igualar ou ultrapassar o país B')