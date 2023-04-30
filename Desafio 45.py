from time import sleep
from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
pc = randint(0, 2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if jogador == 0:
    jogador = 'PEDRA'
    if pc == 1:
        pc = 'PAPEL'
        print('COMPUTADOR VENCE')
    elif pc == 2:
        pc = 'TESOURA'
        print('JOGADOR VENCE')
    else:
        pc = 'PEDRA'
        print('EMPATE. JOGUE DE NOVO!')
if jogador == 1:
    jogador = 'PAPEL'
    if pc == 0:
        pc = 'PEDRA'
        print('JOGADOR VENCE')
    elif pc == 2:
        pc = 'TESOURA'
        print('COMPUTADOR VENCE')
    else:
        pc = 'PAPEL'
        print('EMPATE. JOGUE DE NOVO!')
if jogador == 2:
    jogador = 'TESOURA'
    if pc == 0:
        pc = 'PEDRA'
        print('COMPUTADOR VENCE')
    elif pc == 1:
        pc = 'PAPEL'
        print('JOGADOR VENCE')
    else:
        pc = 'TESOURA'
        print('EMPATE. JOGUE DE NOVO!')
print('-=' * 10)
print('Computador jogou {}'.format(pc))
print('Jogador jogou {}'.format(jogador))
print('-=' * 10)