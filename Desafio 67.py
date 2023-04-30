while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n > 0:
        for c in range(1, 11):
            print(f'{n} x {c:2} = {n * c}')
            c += 1
    if n < 0:
        break
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
