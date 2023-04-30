peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 < imc <= 25:
    print('PARABÉNS! Você está no PESO IDEAL!')
elif 25 < imc <= 30:
    print('Você está com SUBREPESO!')
elif 30 < imc <= 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')
