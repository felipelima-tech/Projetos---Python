nome = str(input('Digite seu nome completo:')).upper().strip().capitalize()

nome = nome.split()

print('Muito prazer em te conhecer')
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu ultimo nome é: {nome[len(nome) - 1]}')