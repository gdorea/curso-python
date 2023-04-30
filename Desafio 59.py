from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('>>>>> Qual é a sua opção? '))
    if escolha == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
    elif escolha == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
sleep(1)
print('Fim do programa! Volte sempre!')
