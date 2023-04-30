soma = cont = maior = menor = 0
c = 'S'
while c in 'Ss':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    soma = soma + n
    if cont == 1:
       maior = menor = n
    else:
        if n > maior:
            meior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média foi {:.2f}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
