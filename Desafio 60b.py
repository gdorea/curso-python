from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(n)
print('Calculando {}!'.format(n), end=' = ')
for c in range(n, 0, -1):
    if c > 1:
        print(c, end=' x ')
    else:
        print(c, '=', end=' ')
print(fatorial)
