#Pra se aposentar tem que ter 35 anos de contribuição
from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - ano
carteira = int(input('Carteira de trabalho (0 não tem): '))
cadastro['ctps'] = carteira
if carteira != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (35 - (date.today().year - cadastro['contratação'])) + cadastro['idade']
print('-=' * 30)
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')
