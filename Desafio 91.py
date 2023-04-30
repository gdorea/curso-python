from random import randint
dados = {}
maior = 0
for c in range(0, 4):
    dados[f'jogador{c+1}'] = randint(1, 6)
print('Valores sorteados: ')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
#ver a resposta de como colocar em ordem na aba Desafio 91b
