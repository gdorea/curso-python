matriz = [[], [], []]
for v1 in range(0, 3):
    for v2 in range(0, 3):
        if v1 == 0:
            matriz[0].append(int(input(f'Digite um valor para [{v1}, {v2}]: ')))
        elif v1 == 1:
            matriz[1].append(int(input(f'Digite um valor para [{v1}, {v2}]: ')))
        elif v1 == 2:
            matriz[2].append(int(input(f'Digite um valor para [{v1}, {v2}]: ')))
print('-=' * 30)
for v1 in range(0, 3):
    for v2 in range(0, 3):
        print(f'[ {matriz[v1][v2]} ]', end=' ')
    print()
