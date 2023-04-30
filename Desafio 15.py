dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
aluguel = dias * 60 + km * 0.15
print('O total a pagar é de R$ {:.2f}'.format(aluguel))

# o carro custa 60 reais por dia e 0,15 por km rodado