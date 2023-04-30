times = ('Corinthians', 'Palmeiras', 'Ferroviária', 'Santos',
         'São Paulo', 'Cruzeiro', 'Grêmio', 'Real Brasília', 'Flamengo',
         'Internacional', 'Bahia', 'Atlhetico-PR', 'Atlético-MG',
         'Avaí', 'Real Ariquemes', 'Ceará')
print('-=' * 30)
print(f'Lista de times do Brasileirão Feminino: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 30)
print(f'Times em orgem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Bahia está na {times.index("Bahia")+1}ª posição')
