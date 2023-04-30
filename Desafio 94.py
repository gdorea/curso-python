dados = {}
cadastro = []
somaidade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    somaidade += dados['idade']
    cadastro.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
print(f'B) A média de idade é de {somaidade / len(cadastro):.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for c in range(0, len(cadastro)):
    if cadastro[c]['sexo'] == 'F':
        print(cadastro[c]['nome'], end=' ')
    else:
        c += 1
print(f'\nD) Lista das pessoas que estão acima da média:')
for c in range(0, len(cadastro)):
    if (somaidade / len(cadastro)) < cadastro[c]['idade']:
        print(cadastro[c])
print('<< ENCERRADO >>')
