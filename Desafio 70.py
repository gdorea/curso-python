total = tot1000 = menor = cont = 0
barato = ''
print('-' * 30)
print('LOJA SUPER FONTES')
print('-' * 30)
while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        tot1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 10, ' FIM DO PROGRAMA ', '-' * 10)
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
