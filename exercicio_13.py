numero = int(input('Digite um número inteiro positivo: '))

cont = 2

if numero < 2:
    print('Não é primo.')
else:
    while cont < numero:
        if numero % cont == 0:
            break
        cont += 1

    if cont == numero:
        print(f'O número {numero} é primo.')
    else:
        print(f'O número {numero} não é primo.')