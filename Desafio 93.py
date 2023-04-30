jogador = {}
partidas = []
soma = 0
jogador['nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, n):
    quant = int(input(f'Quantos gols na partida {c+1}? '))
    partidas.append(quant)
    soma += quant
jogador['gols'] = partidas[:]
jogador['total'] = soma
#jogador['total'] = sum(partidas) -> Outra forma de fazer a soma, de um jeito mais simples.
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {n} partidas.')
#print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"]} partidas.') -> Outra forma de pegar a quantidade de partidas.
for i, v in enumerate(partidas): #pode ser também enumerate(jogador['gols'])
    print(f' => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {soma} gols.') #podemos declarar a soma como {jogador["total"]}
