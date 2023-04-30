from random import randint
def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
    print('PRONTO!')


def somaPar(lista):
    spares = 0
    for cont in lista:
        if cont % 2 == 0:
            spares += cont
    print(f'Somando os valores pares de {lista}, temos {spares}')


números = []
sorteia(números)
somaPar(números)
