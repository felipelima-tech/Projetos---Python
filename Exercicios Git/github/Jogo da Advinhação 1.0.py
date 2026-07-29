from random import randint
from time import sleep

print('-=-' * 35 )
print('Vou pensar em um número de 0 a 10. Tente advinhar...')
print('-=-' * 35)

pensando = randint(0,10)

numero = int(input('Em que número eu pensei ?'))

print('PENSANDO...')
sleep(2)

if pensando == numero:
    print('PARABÉNS ! Você advinhou o número')
else:
    print(f'GANHEI! Eu pensei no numero {pensando} e não no {numero}!')