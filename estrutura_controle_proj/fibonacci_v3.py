#!/usr/local/bin/python3

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=',')

if __name__ == '__main__':
    fibonacci(10000)
