from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if atual - ano < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade \nE também tivemos {} pessoas menores de idade'.format(maior, menor))

# maior de idade vai ser maior de 21 anos