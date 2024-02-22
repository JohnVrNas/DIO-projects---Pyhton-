#for
n = int(input("Quantos valores você deseja calcular a média? "))
soma = 0
for i in range(n):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    soma += valor
media = soma / n
print(f"A média dos {n} valores é: {media:.2f}")

#while
soma = contagem = 0
n = int(input("Quantos valores você deseja calcular a média? "))
while contagem < n:
    valor = float(input(f"Digite o {contagem + 1}º valor: "))
    soma += valor
    contagem += 1
media = soma / n
print(f"A média dos {n} valores é: {media}")