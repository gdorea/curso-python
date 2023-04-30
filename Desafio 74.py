from random import sample
lista = sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=5)
print(f'Os valores sorteados foram: {lista}')
print(f'O maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')
