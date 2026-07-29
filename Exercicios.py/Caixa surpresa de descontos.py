from random import choice

nome_cliente = input('Nome do cliente:')

valor_compra = float(input('Valor da compra;'))

lista = [5,10,15,20,25,30]

desconto = choice(lista)

if desconto <= 10:
    print('Você ganhou um desconto comum')
elif desconto <= 20:
    print('Você ganhou um bom desconto')
else:
    print('Parabés!, você ganhou o maior desconto!')


valor_final = valor_compra - desconto

porcentagem = valor_compra * desconto / 100

print(f'Desconto sorteado {desconto}%')

print(f'Valor descontado {porcentagem}')

print(f'Valor final R${valor_final}')
