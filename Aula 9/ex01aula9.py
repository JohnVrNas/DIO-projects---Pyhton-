import os
os.system('cls')
tentativa = 0
print('Digite um número entre 1 até 10')
jog1 = int(input('Jogador 1: '))
while jog1 < 1 or jog1 > 10:
    print(' Número fora do intervalo! Digite novamente')
    print('Digite um número entre 1 até 10')
    jog1 = int(input('Jogador 1:' ))
print('=-'*15)
print('Agora o jogador 2 tem que adivinhar...')
print('=-'*15)
print('Digite um número entre 1 até 10:' )
jog2 = int(input('Jogador 2:' ))
while jog2 < 1 or jog2 > 10:
    print(' Número fora do intervalo! Digite novamente')
    print('Digite um número entre 1 até 10:' )
    jog2 = int(input('Jogador 2:' ))
while jog1 != jog2:
    print('Errou!! Tente Novamente')
    print('=-'*15)
    tentativa += 1
    print('Digite um número entre 1 até 10:' )
    jog2 = int(input('Jogador 2:' ))
    print('=-'*15)
    while jog1<1 or jog2>10:
        print('Número fora do intervalo!! Tente Novamente')
        print('Digite um número entre 1 até 10:' )
        jog2 = int(input('Jogador 2:' ))
        print('=-'*15)
print('Você acertou!! Parabéns!!!')
print(f'Número de tentativa: {tentativa+1}')

            
