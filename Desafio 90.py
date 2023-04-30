boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['media'] >= 7:
    boletim['situação'] = 'Aprovado'
elif 5 <= boletim['media'] < 7:
    boletim['situação'] = 'Recuperação'
elif boletim['media'] < 5:
    boletim['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in boletim.items():
    print(f'- {k} é igual a {v}')
