num = int(input('Digite um numero: '))

print('\n******** Tabuada de Adicao ********\n')

for n in range(1, 11):
    r = num + n
    print(num, ' + ', n, ' = ', r)

print('\n******** Tabuada de Subtracao ********\n')

for n in range(1, 11):
    r = n - num
    print(n, ' - ', num, ' = ', r)

print('\n******** Tabuada de Multiplicacao ********\n')

for n in range(1, 11):
    r = num * n
    print(num, ' x ', n, ' = ', r)

print('\n******** Tabuada de Divisao ********\n')

for n in range(1, 11):
    r = num / n
    print(num, ' / ', n, ' = ', round(r, 2))
