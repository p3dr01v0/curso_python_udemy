#!/usr/local/bin/python3

#soma de 1 em 1
# def fibonacci():
#     penultimo = 0
#     ultimo = 1
#     while True:
#         proximo = penultimo + ultimo
#         print(proximo, end=',')
#         penultimo = 1
#         ultimo = proximo

# if __name__ == '__main__':
#     fibonacci()


#soma o ultimo mais o penultimo
def fibonacci():
    penultimo = 0
    ultimo = 1
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo
        
if __name__ == '__main__':
    fibonacci()
