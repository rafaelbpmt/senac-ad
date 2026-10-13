numero = int(input("Digite um número: "))

cont = 1

print('Os divisores são: ')

while cont <= numero:
    if numero % cont == 0:
        print (cont, end=' ')
    cont += 1