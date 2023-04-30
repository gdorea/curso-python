valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print(f'Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado! Não vou adicionar...')
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print('-=' * 40)
valores.sort()
print(f'Você digitou os valores {valores}')
