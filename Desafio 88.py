from random import randint
from time import sleep
print('-' * 30)
print('JOGO DA MEGA SENA')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
mega = []
prov = []
for l in range(0, jogos):
    for c in range(0, 6):
        n = randint(1, 60)
        prov.append(n)
    mega.append(prov[:])
    prov.clear()
print('-=' * 3, f' SORTEANDO {jogos} JOGOS ', '-=' * 3)
sleep(0.5)
for c in range(0, jogos):
    print(f'Jogo {c+1}: {mega[c]}')
    sleep(0.5)
print(f'-=' * 3, ' BOA SORTE ', '-=' * 3)
