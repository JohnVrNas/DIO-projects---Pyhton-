print('Somatória de número')
s = 0
n =  int(input('Digite o número máximo: '))
for i in range(0, n+1):
    s += i
    print(i)
print(s)