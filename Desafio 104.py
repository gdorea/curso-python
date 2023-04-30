def leiaInt(num):
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            return num
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
