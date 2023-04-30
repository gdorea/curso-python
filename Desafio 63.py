print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
termos = int(input('Quantos termos você quer mostrar? '))
c = 0
c2 = 0
c3 = 1
while c < termos:
    print(c2, end=' -> ')
    c4 = c2 + c3
    c3 = c2
    c2 = c4
    c += 1
print('FIM')