print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(termo, end=' -> ')
    termo += razão
    c += 1
print('FIM')
