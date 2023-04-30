números = [int(input(f'Digite um valor para a Posição 0: ')),
           int(input(f'Digite um valor para a Posição 1: ')),
           int(input(f'Digite um valor para a Posição 2: ')),
           int(input(f'Digite um valor para a Posição 3: ')),
           int(input(f'Digite um valor para a Posição 4: '))]
print('=-' * 30)
print(f'Você digitou os valores {números}')
print(f'O maior valor digitado foi {max(números)} nas posições', end=' ')
for pos in range(0, len(números)):
    if números[pos] == max(números):
        print(pos, end='... ')
print(f'\nO menor valor digitado foi {min(números)} nas posições ', end='')
for pos in range(0, len(números)):
    if números[pos] == min(números):
        print(pos, end='... ')
