lista = []
for n in range(0, 5):
    pos = int(input('Digite um valor: '))
    if n == 0 or pos > lista[-1]:
        lista.append(pos)
        print('Adicionado ao final da lista...')
    else:
        p = 0
        while p < len(lista):
            if pos <= lista[p]:
                lista.insert(p, pos)
                print(f'Adicionado na posição {p} da lista...')
                break
            p += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
