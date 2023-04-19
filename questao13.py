num = input('\nDigite uma lista de numeros separado por espaco: ')

lista = [int(numero) for numero in num.split()]

ordem_cres = sorted(lista)

print(f'\nLista em ordem Crescente:\n{ordem_cres}\n')
