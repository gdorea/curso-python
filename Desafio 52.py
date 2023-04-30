cont = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print('\033[33m', c, '\033[m', end='')
    else:
        print('\033[31m', c, '\033[m', end='')
print('\nO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

