from generators_v1 import cores_arco_iris


def sequencia():
    num = 0
    while True:
        num += 1
        yield num


if __name__ == '__main__':
    generator = cores_arco_iris()
    for cor in generator:
        print(cor)
    print('Fim!')

    seq = sequencia()
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
