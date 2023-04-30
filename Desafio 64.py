c = n = soma = 0
while c != 999:
    c = int(input('Digite um número [999 para parar]: '))
    if c != 999:
        n += 1
        soma = soma + c
print('Você digitou {} números e a soma entre eles foi {}'.format(n, soma))
