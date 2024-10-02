def sequencia_fibonacci(n):
    fib = [0,1]

    while fib[-1] < n:
        prox = fib[-1] + fib[-2]
        fib.append(prox)

    return fib


def em_fibonacci(n):

    fib = sequencia_fibonacci(n)

    if n in fib:
        return f'O número {n} existe na sequência.'
    else:
        return f'O número {n} não existe na sequência.'

numero = int(input('Digite um número: '))
print(em_fibonacci(numero))
        
