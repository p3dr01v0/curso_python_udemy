# entendendo a função sum
soma_um = sum([1, 2])
soma_dois = sum([3, 4])
soma = sum([soma_um, soma_dois])

print(soma)

# testando a função sum
# def fibonacci(limite):
#     penultimo = 0
#     ultimo = 1
#     while ultimo < limite:
#         soma = sum([penultimo, ultimo])
#         penultimo = ultimo
#         ultimo = soma
#         print(soma, end=',')


# if __name__ == '__main__':
#     fibonacci(15000)


# resposta chegada
# def fibonacci(limite):
#     lista = [0, 1]
#     while lista[-1] < limite:
#         soma = sum([lista[-2], lista[-1]])
#         lista[-1] = soma
#         lista[-2] = lista[-1]
#         print(soma, end=',')


# if __name__ == '__main__':
#     fibonacci(15000)


# resposta professor
def fibonacci(limite):
    resultado = [0, 1]
    # o "[-1]" se refere ao indeice ou seja o ultimo resultado
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib,)
