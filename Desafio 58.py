from random import randint
vezes = 0
print('''Oi! Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
pc = randint(0, 10)
n = int(input('Qual é o seu palpite? '))
while pc != n:
    if pc > n:
        n = int(input('Mais... Tente mais uma vez. '))
    if pc < n:
        n = int(input('Menos... Tente mais uma vez. '))
    vezes += 1
print('Acertou com {} tentativas. Parabéns!'.format(vezes + 1))
