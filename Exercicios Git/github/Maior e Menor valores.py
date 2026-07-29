primeiro = int(input('Digite o primeiro valor:'))

segundo = int(input('Digite o segundo valor:'))

terceiro = int(input('Digite o terceiro valor:'))

if primeiro < segundo and primeiro < terceiro:
    menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')