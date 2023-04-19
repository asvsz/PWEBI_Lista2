num = input('Digite uma lista de numeros separado por espaco: ')

lista = [int(numero) for numero in num.split()]

media = sum(lista) / len(lista)

print(f'\nA media da lista e: {round(media,2)}\n')
