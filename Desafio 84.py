lista = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {lista}')
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {menor} Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]} ', end='')