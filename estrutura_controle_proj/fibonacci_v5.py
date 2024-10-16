#!/usr/local/bin/python3

def fibonacci(limite):
    resultado = [0, 1]
    # o "[-1]" se refere ao indeice ou seja o ultimo resultado
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)
