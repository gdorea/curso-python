from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano = date.today().year #Pega o ano atual
idade = ano - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))
if idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(ano - (idade - 18)))
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(ano + (18 - idade)))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
