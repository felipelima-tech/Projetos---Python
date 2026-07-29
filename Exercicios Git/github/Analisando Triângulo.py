print('-=-' * 15)
print('         ANALISADOR DE TRIÂNGULO   ')
print('-=-' * 15)

s1 = float(input('Primeiro Segmento:'))
s2 = float(input('Segundo Segmento:'))
s3 = float(input('Terceiro Segmento:'))

if s1 < s2 + s3 and s2< s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo!!')
else:
    print('Os segmentos acima não podem formar um triângulo!!')

