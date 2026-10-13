nota_01 = float(input('Digite a primeira nota: '))
nota_02 = float(input('Digite a segunda nota: '))
nota_03 = float(input('Digite a terceira nota: '))
nota_04 = float(input('Digite a quarta nota: '))
resultado_final = (nota_01 + nota_02 + nota_03 + nota_04) / 4 

if resultado_final >= 7.5:
    print('Aprovado!')
else:
    print('Reprovado!')