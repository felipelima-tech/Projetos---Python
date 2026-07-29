nome_cliente = input('Nome do Cliente:')

idade = int(input('Idade:'))

renda_mensal = float(input('Renda Mensal:'))

cidade = input('Cidade:')

profissao = input('Profissão:')

renda_anual = renda_mensal * 12

renda_parcial = renda_mensal * 0.30

if renda_mensal < 2000:
    print('Renda Baixa')
elif renda_mensal >= 2000 and renda_mensal < 5000:
    print('Renda Média')
else:
    print('Alta Renda')

valor_empréstimo = float(input('Valor desejado do Empréstimo:'))

qtd_parcelas = int(input('Quantidade de parcelas:'))

valor_parcela = valor_empréstimo / qtd_parcelas

juros5 = valor_parcela * 0.05

juros10 = valor_parcela * 0.10

juros15 = valor_parcela * 0.15

if qtd_parcelas <= 12:
    valor_parcela = valor_parcela + juros5
elif qtd_parcelas >= 13 and qtd_parcelas <= 24:
    valor_parcela = valor_parcela + juros10
else:
    valor_parcela = valor_parcela + juros15

if idade >= 18 and idade <= 65 and renda_mensal >= 1500 and valor_parcela <= renda_parcial:
    print('Empréstimo Aprovado')
else:
    print('Empréstimo Negado')
    valor_parcela = 0

from random import choice

beneficios = ['Cartão sem anuidade', 'Cashback de 5%', 'Seguro gratuito', 'Consultoria financeira']

beneficio = choice(beneficios)

print(f'Nome:{nome_cliente}')
print(f'Idade:{idade}')
print(f'Cidade: {cidade}')
print(f'Profissão: {profissao}')
print(f'Renda Mensal: R${renda_mensal}')
print(f'Renda Anual: R${renda_anual}')
print(f'Parcelas:{qtd_parcelas}x')
print(f'Sua parcela será no valor de R$:{valor_parcela:.2f}')
if valor_parcela > 1:
    print(f'Benefício recebido:{beneficio}')
elif valor_parcela == 0:
    print('Sem benefício')