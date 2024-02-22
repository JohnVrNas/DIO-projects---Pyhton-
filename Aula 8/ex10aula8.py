cont = 0
N = int(input("Digite a quantidade de números: "))
for i in range(N):
    num = int(input("Digite o número: "))
    if num % 2 == 0:
        cont += 1
print(f"{cont} números são pares")

    


