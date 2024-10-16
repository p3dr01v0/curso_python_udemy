with open("info.csv") as info:
    with open("dados.txt", "w") as dados:
        for registro in info:
            formatado = registro.strip().split(",")
            print('nome: {}, idade{}, id:{}' .format(*formatado), file=dados)
