lista1 = []
listapar = []
listaimpar = []
while True:
    lista1.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'A lista completa é {lista1}')
for n, v in enumerate(lista1):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'A lista de pares é {listapar}')
print(f'A losta de ímpares é {listaimpar}')
