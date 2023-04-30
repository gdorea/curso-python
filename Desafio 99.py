def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    mvalor = 0
    for c in num:
        if c > mvalor:
            mvalor = c
    for c in num:
        print(f'{c}', end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mvalor}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
