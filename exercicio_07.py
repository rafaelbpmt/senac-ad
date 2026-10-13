entrada01 = int(input('insira o primeiro número: '))
entrada02 = int(input('insira o segundo número: '))
entrada03 = int(input('insira o terceiro número: '))

if entrada01 > entrada02 and entrada01 > entrada03:
    print('O primeiro número informado é o maior.')
elif entrada02 > entrada01 and entrada02 > entrada03:
    print('O segundo número informado é o maior.')
elif entrada03 > entrada01 and  entrada03 > entrada02:
    print('O terceiro número é o maior.')
elif entrada01 == entrada02 and entrada01 == entrada02 and entrada01 == entrada03:
    print('Os números são iguais.')