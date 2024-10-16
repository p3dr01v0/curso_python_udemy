def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':

    # packing, esta ocorrendo o empacotamento dos valores e então sendo repassados para a função como parametros
    print(soma_2(2, 3))
    print(soma_3(2, 3, 4))
    print(soma_n(2, 3, 4, 5, 6, 7))

    # unpacking, estamos pegando a tupla e lista e a desempacotando, passando assim os valores como os parametros
    tuple_nums = (1, 2, 3, 4, 5, 6, 7)
    print(soma_n(*tuple_nums))

    lista_nums = [2, 3, 4]
    print(soma_n(*lista_nums))
