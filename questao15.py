num = input('\nDigite uma lista de numeros separado por espaco: ')

x = int(input('\nDigite o numero X: '))

lista = [int(numero) for numero in num.split()]

if x in lista:
    print(f'\nO numero {x} esta na lista!\n')
else:
    print(f'\nO numero {x} nao esta na lista!\n')
