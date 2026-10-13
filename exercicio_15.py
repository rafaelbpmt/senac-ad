numero01 = int(input('Digite o primeiro número inteiro: '))

numero02 = int(input('Digite o segundo número inteiro: '))

if numero01 < numero02:
    mdc = numero01
else:
    mdc = numero02

while numero01 % mdc != 0 or numero02 % mdc != 0:
    mdc -= 1

print('O mdc é:', mdc)