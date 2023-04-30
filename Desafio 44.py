print('{:=^40}'.format(' LOJAS FONTES '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 0.1)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    print('Sua compra será parcelada em 2x SEM JUROS de R$ {:.2f}'.format(total / 2))
elif opção == 4:
    parcelas = int(input('Quantas parcelas vão ser? '))
    total = preço + (preço * 0.2)
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(parcelas, total / parcelas))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))
