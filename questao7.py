n = int(input('Digite um numero: '))


def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)


for i in range(0, n):
    print(fib(i), end=' ')
