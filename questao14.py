num = input('\nDigite uma lista de numeros separado por espaco: ')

lista = [int(numero) for numero in num.split()]

ordem_decre = sorted(lista, reverse=True)

print(f'\nLista em ordem Decrescente:\n{ordem_decre}\n')
