jogador = {}
partidas = []
tabela = []
while True:
    partidas.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    soma = 0
    for c in range(0, n):
        quant = int(input(f'Quantos gols na partida {c+1}? '))
        partidas.append(quant)
        soma += quant
    jogador['gols'] = partidas[:]
    jogador['total'] = soma
    tabela.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N para continuar.')
    if resp == 'N':
        break
print('-=' * 20)
print('cod.  nome     gols        total')
print('-' * 40)
c = 0
for p in tabela:
    print(f'{c}  {p["nome"]}   {p["gols"]}   {p["total"]}')
    c += 1
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(tabela):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' == LEVANTAMENTO DO JOGADOR {tabela[busca]["nome"]}:')
        for i, g in enumerate(tabela[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')
