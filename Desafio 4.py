dig = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(dig))
print('Só tem espaços?', dig.isspace())
print('É um número?', dig.isnumeric())
print('É alfabético?', dig.isalpha())
print('É alfanumérico?', dig.isalnum())
print('Está em maiúsculas?', dig.isupper())
print('Está em minúsculas?', dig.islower())
print('Está capitalizada?', dig.istitle())

