lista_um = [1, 2]


def juncao():
    while True:
        lista_um[-1] = lista_um[-2] + lista_um[-1]
        print(lista_um[-1], end=',')


print(juncao())
