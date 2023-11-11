from time import sleep
resultado = 0
vezes=int(input('Quantas vezes a operação deve ser feita? :' ))

print('\n')

operação=int(input('Qual operação você deseja fazer?\nMultiplicação [1] \nDivisão [2] \nSoma[3] \nSubtração [4] \n'))

if operação == 1:
    segundonumero = float(input('por quanto ele será multiplicado? :'))

if operação == 2:
    segundonumero = float(input('por quanto ele será dividido? :'))

if operação == 3:
    segundonumero = float(input('por quanto ele será somado? :'))

if operação == 4:
    segundonumero = float(input('por quanto ele será subritaido? :'))

print('\n')

if operação == 1 :
    for vezes in range (0, vezes):
            numero = float(input('Qual o numero? :'))
            resultado = numero * segundonumero 
            print(resultado, '\n')

if operação == 2 :
    for vezes in range (0, vezes):
            numero = float(input('Qual o numero? :'))
            resultado = numero / segundonumero 
            print(resultado, '\n')

if operação == 3 :
    for vezes in range (0, vezes):
            numero = float(input('Qual o numero? :'))
            resultado = numero + segundonumero 
            print(resultado, '\n')

if operação == 4 :
    for vezes in range (0, vezes):
            numero = float(input('Qual o numero? :'))
            resultado = numero - segundonumero 
            print(resultado ,'\n')