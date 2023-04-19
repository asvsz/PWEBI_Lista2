num = input('\nDigite uma lista de números separado por espaco: ')

lista = [int(numero) for numero in num.split()]

print('\n******   Todos os numeros pares da lista sao   ******\n')

for i in lista:
    if i % 2 == 0:
        print(i, end=' ')
