numero = int(input('Digite um número qualquer:'))

resultado = numero % 2
if resultado == 0:
    print(f'Número {numero} é par')
else:
    print(f'Número {numero} é impar')