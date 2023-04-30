def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) motrar ou não a conta.
    :return: o valor do Fatorial de um número n.
    """
    resultado = 1
    for c in range(n, 0, -1):
        resultado *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return print(resultado)


fatorial(5, show=True)
