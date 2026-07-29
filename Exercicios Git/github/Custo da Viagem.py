distancia = float(input('Qual é a distância da viagem ?'))

print(f'Você esta prestes a começar uma viagem de {distancia}Km.')

if distancia >= 250:
    custo = distancia * 0.45
else:
    custo = distancia * 0.50

print(f'E o preço da sua passagem é de R${custo:.2f}')