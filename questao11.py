num = input('\nDigite uma lista de numeros separado por espaco: ')

lista = [int(numero) for numero in num.split()]

print('\n******   Todos os numeros impares da lista sao   ******\n')

for i in lista:
    if i % 2 != 0:
        print(i, end=' ')
