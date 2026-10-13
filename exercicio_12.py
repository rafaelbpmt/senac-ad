numero = int(input('Digite um número: '))

if numero == 0:
    quantidade = 1
else:
    quantidade = 0
    while numero > 0:
        numero = numero // 10
        quantidade += 1

print('Quantidade de digitos:', quantidade)