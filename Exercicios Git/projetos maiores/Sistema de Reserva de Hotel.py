from random import choice
from time import sleep

nome = str(input('Nome:'))

idade = int(input('Idade:'))

cidade = str(input('Cidade:'))

qtd_noite = int(input('Quantidade de noites:'))

print('''==========MENU==========
    Standard (R$ 180 por noite)
    Luxo (R$ 280 por noite)
    Premium R$ 450 por noite''')

quarto = str(input('Quarto desejado:'))

if quarto.lower().strip() == 'standard':
    valor_total = 180 * qtd_noite
if quarto.lower().strip() == 'luxo':
    valor_total = 280 * qtd_noite
if quarto.lower().strip() == 'premium':
    valor_total = 450 * qtd_noite

if qtd_noite >= 7:
    valor_final = valor_total - (valor_total * 18 / 100)
if qtd_noite >= 4 and qtd_noite <= 6:
    valor_final = valor_total - (valor_total * 8 / 100)
else:
    valor_final = valor_total

if idade < 18:
    print('Menor de idade')
if idade >= 18 and idade <= 59:
    print('Adulto')
if idade >= 60:
    print('Maior idade')

forma_pagamento = str(input('Forma de pagamento:'))

if forma_pagamento.lower().strip() == 'pix':
    valor_desconto = valor_final - (valor_final * 10 / 100)
if forma_pagamento.lower().strip() == 'dinheiro':
    valor_desconto = valor_final - (valor_final * 5 / 100)
else:
    valor_desconto = valor_final

beneficios = ['Café da manhã VIP', 'Upgrade de quarto', 'Late Chek-out', 'Estacionamento gratuito']

beneficio = choice(beneficios)

print('=' * 15)
print('RESERVA HOTEL')
print('=' * 15)

print('CARREGANDO CADASTRO...')
sleep(3)

print(f'Nome:{nome}')
print(f'Cidade:{cidade}')
print(f'Quarto escolhido:{quarto}')
print(f'Quantidade de noites:{qtd_noite}')
print(f'Valor original:R${valor_total:.2f}')
if forma_pagamento.lower().strip() == 'pix':
    print('Desconto: 10%')
if forma_pagamento.lower().strip() == 'dinheiro':
    print('Desconto: 5%')
print(f'Valor final:R${valor_desconto:.2f}')
print(f'Benefício:{beneficio}')

if quarto.lower() in ['standard', 'luxo', 'premium']:
    print('Reserva válida')
else:
    print('Reserva inválida')

if qtd_noite == 0:
    print('Reserva inválida')

print('=' * 15)
