nome = str(input('Qual é o seu nome completo? ')).strip()
nome = nome.upper()
sil = 'SILVA' in nome
print('Seu nome tem Silva? {}'.format(sil))

#Outra forma de fazer:
#print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))