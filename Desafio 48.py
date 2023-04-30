soma = 0
impares = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma = soma + c # pode ser soma += c
        impares = impares + 1 # pode ser impares += 1
print('A soma de todos os {} valores solicitados é {}'. format(impares, soma))
