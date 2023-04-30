from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
usuario = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
pc = randint(0, 5) # Faz o compurador "Pensar"
print('PROCESSANDO...')
sleep(2) #Dá uma pausa antes de processar os outros comandos abaixo
if usuario == pc:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(pc, usuario))

