sidade = 0
idadevelho = 0
smulher = 0
for c in range(1, 5):
    print('-' * 5, ' {}ª PESSOA '.format(c), '-' * 5)
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    sidade += idade
    if idadevelho < idade and sexo == 'M':
        idadevelho = idade
        nomevelho = nome
    if idade < 20 and sexo == 'F':
        smulher += 1
print('A média de idade do grupo é de {} anos'.format(sidade / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(idadevelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(smulher))
