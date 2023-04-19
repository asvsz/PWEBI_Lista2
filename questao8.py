num = input('Digite uma lista de numeros separado por espaco: ')

lista = [int(numero) for numero in num.split()]

maior = max(lista)
menor = min(lista)

print(f'O maior numero na lista e: {maior}')
print(f'O menor numero na lista e: {menor}')
