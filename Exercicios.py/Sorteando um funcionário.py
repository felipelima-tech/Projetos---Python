import random

p1 = input('Funcionário: ')

p2 = input('Funcionário: ')

p3 = input('Funcionário: ')

p4 = input('Funcionário: ')

p5 = input('Funcionário: ')

lista = [p1,p2,p3,p4,p5]

resultado = random.choice(lista)

print(f'O vencedor do sorteio foi:{resultado}')