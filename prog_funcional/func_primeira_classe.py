def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == '__main__':
    d = dobro
    q = quadrado

    print(d(5))
    print(q(5))

    # o "*5" faz com que a lista se repita 5 vezes
    lista_funcao = [dobro, quadrado] * 5

    # o metodo "zip" nos permite compactar os elementos que estão dentro dos parenteses
    for funcao, numero_range in zip(lista_funcao, range(1, 11)):
        print(
            f'O {funcao.__name__} de {numero_range} = {funcao(numero_range)}')
