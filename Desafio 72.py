lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quize', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    c = int(input('Digite um número entre 0 e 20: '))
    if 0 <= c <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {lista[c]}')
