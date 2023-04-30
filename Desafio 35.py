print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
teste1 = bool(abs(l2 - l3) < l1 < l2 + l3)
teste2 = bool(abs(l1 - l3) < l2 < l1 + l3)
teste3 = bool(abs(l1 - l2) < l3 < l1 + l2)
if teste1 == True and teste2 == True and teste3 == True:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

#Outra forma de condicional:
#if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2: