lista = []
cont = num5 = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
    if num == 5:
        num5 = 1
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print('-=' * 30)
print(f'Os números digitados foram: {lista}')
print(f'Foram digitados {cont} números')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente é {lista}')
if num5 == 1:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')
