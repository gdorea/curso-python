n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0].capitalize()))
print('Seu último nome é {}'.format(nome[len(nome)-1].capitalize()))

#Essa função len está pegando a quantidade de nomes na lista nome.