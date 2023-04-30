alunos = []
prev = []
media = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    prev.append(nome)
    prev.append(n1)
    prev.append(n2)
    prev.append(media)
    alunos.append(prev[:])
    prev.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print('No.   NOME        MÉDIA')
print('-' * 30)
for c in range(0, len(alunos)):
    print(f'{c}   {alunos[c][0]:<4}       {alunos[c][len(alunos)]:>6}')
print('-' * 30)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for i in range(0, len(alunos)):
        if notas == i:
            print(f'Notas de {alunos[notas][0]} são {alunos[notas][1]} e {alunos[notas][2]}')
    if notas == 999:
        break
print('FINALIZANDO...')
print('<<<< VOLTE SEMPRE >>>>')