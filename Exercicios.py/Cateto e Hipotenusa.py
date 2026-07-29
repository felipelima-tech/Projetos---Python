from math import hypot

cateto_oposto = float(input('Comprimento do Cateto Oposto:'))

cateto_adjacente = float(input('Comprimento do Cateto Adjacente:'))

hipotenusa = hypot(cateto_oposto,cateto_adjacente)

print(f'A Hipotenusa vai medir {hipotenusa:.2f}')