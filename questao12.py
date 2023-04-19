num = input('\nDigite uma lista de numeros separado por espaco: ')

lista = [int(numero) for numero in num.split()]

soma = sum(lista)

print(f'\nA soma da lista e: {soma}\n')
