nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print('Seu nome tem ao todo {} letas'.format(len(nome) - nome.count(' ')))
primeiro = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro[0],len(primeiro[0])))

