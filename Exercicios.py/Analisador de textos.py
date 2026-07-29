nome = str(input('Digite seu nome completo:'))

print(f'O nomme completo é: {nome.upper()}')
print(f'O nome completo é: {nome.lower()}')

contagem = len(nome)

separa = nome.split()

print(f'O nome tem {contagem} letras')

print(f'O seu primeiro nome é {separa[0]}')

print(f'O seu primeiro nome tem {len(separa[0])} letras')


