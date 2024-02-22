print('Ao Quadrado')
resp = ''
while resp in 'S':
    numero = float(input('Digite um número: '))
    quadrado = numero**2
    print(quadrado)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print('Volte Sempre!')


n = int(input('Digite um número de repetições: '))
for c in range(1,n+1):
    n = int(input('Digite um número: '))
    q = n**2
    print(f'O valor elevado foi {q}')