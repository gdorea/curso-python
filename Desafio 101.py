from datetime import datetime


def voto(i):
    print(f'Com {i} anos: ', end='')
    if i < 16:
        print('VOTO NEGADO')
    elif 18 <= i < 65:
        print('VOTO OBRIGATÓRIO')
    else:
        print('VOTO OPCIONAL')


ano = datetime.today().year
print('-' * 30)
nascimento = int(input('Em que ano você nasceu? '))
idade = ano - nascimento
voto(idade)
