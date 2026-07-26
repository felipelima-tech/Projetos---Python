nome_cliente = input('Nome do cliente:')

salario_mensal = float(input('Salário Mensal:'))

valor_empréstimo = float(input('Valor do empréstimo desejado:'))

qtd_parcelas = int(input('Quantidade de parcelas:'))

porcentagem_do_salario = salario_mensal * 0.30

parcela = valor_empréstimo / qtd_parcelas

juros = (parcela * 0.015)

parcelas = juros

if porcentagem_do_salario < parcela:
    print(f'{nome_cliente} Empréstimo negado: parcela ultrapassa limite de renda, pois a parcela é de R$ {parcela:.2f}, com {parcelas:.2f}% de juros')
elif salario_mensal >= 5000:
    print(f'{nome_cliente} Empréstimo Aprovado - Cliente premium, parcela é de R$ {parcela:.2f}, com {parcelas:.2f}% de juros')
else:
    print(f'{nome_cliente} Empréstimo aprovado, suas parcelas são de: R$ {parcela:.2f}, com {parcelas:.2f}% de juros')