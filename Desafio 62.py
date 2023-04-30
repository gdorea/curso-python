print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
c = 1
cont = 10
resultado = cont
while cont != 0:
    while c <= cont:
        print(termo, end=' -> ')
        termo += razão
        c += 1
    print('PAUSA')
    cont = int(input('Quantos termos você quer mostrar a mais? '))
    c = 1
    resultado += cont
print('Progressão finalizada com {} termos mostrados.'.format(resultado))
