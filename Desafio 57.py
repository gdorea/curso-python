sexo = str(input('Informe seu sexo: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input(('Dados inválidos. Por favor, informe seu sexo: '))).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
