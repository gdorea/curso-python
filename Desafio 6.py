n1 = int(input('Digite um número: '))
d2 = n1 * 2
d3 = n1 * 3
rq = n1 ** (1/2)
print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n1,d2,d3,rq))

#Para usar a função interna que calcula a raiz quadrada, poderiamos escrever: pow(n1, (1/2))
