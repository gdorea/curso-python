def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
jogador = str(input('Nome do jogador: '))
ngols = str(input('Número de gols: '))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if jogador.strip() == '':
    ficha(gols=ngols)
else:
    ficha(jogador, ngols)
