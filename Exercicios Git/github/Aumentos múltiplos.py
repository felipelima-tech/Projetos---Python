salario1 =  float(input('Qual o salário do funcionário ?'))

adicional10 = salario1 * 0.10

adicional15 = salario1 * 0.15

if salario1 >= 1250:
    salario = salario1 + adicional10
else:
    salario = salario1 + adicional15

print(f'Quem ganhava R${salario1:.2f}, passa a ganhar R${salario:.2f} ')