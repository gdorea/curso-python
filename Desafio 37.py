n1 = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
n2 = int(input('Sua opção: '))
if n2 == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n1, bin(n1)[2:]))
elif n2 == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n1, oct(n1)[2:]))
elif n2 == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção inválida. Tente novamente!')

