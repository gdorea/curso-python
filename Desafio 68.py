from random import randint
cont = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
while True:
    valorj = int(input('Diga um valor: '))
    parimparj = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    valorpc = randint(1, 11)
    soma = valorj + valorpc
    if soma % 2 == 0:
        resultado = 'P'
        r2 = 'DEU PAR'
    else:
        resultado = 'I'
        r2 = 'DEU ÍMPAR'
    print('-' * 30)
    print(f'Você jogou {valorj} e o computador {valorpc}. Total de {soma} {r2}')
    print('-' * 30)
    if parimparj == resultado:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-=' * 20)
        cont += 1
    else:
        print('Você PERDEU!')
        print('-=' * 20)
        break
print(f'GAME OVER! Você venceu {cont} vezes.')
