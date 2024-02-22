import os
os.system('cls')
print("""5. Elaborar um programa em Python que receba uma lista 
      com 10 valores numéricos, gere uma nova lista onde 
      cada elemento dessa lista é o quadrado dos 
      elementos da primeira lista.""")
num = []
quad = []
for i in range (10):
    num.append(int(input(f'Digite o {i+1}° número: ')))
quad=num[:]
for c in (quad): 
    print(f"número {c} ao quadrado fica {c**2}")
    