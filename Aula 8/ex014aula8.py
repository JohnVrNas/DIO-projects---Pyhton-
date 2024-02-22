m = s = n = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n > 0:
        for s in range(0, 10):
            s += 1
            m = n * s
            print(f'{n} x {s} = {m}')
    else:
        break