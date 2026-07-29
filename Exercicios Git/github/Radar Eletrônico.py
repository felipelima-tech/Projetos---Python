from time import sleep

velocidade = float(input('Qual é a velocidade atual do carro:'))
print('RADAR ANALISANDO...')
sleep(2)

if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')

print('Tenha um bom dia! Dirija com segurança')