from math import hypot
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
hipo = hypot(catop, catad)
print('O comprimento da hipotenusa é {:.2f}'.format(hipo))


'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
A hipotenusa é igual a raiz quadrada da soma dos catetos ao quadrado'''
