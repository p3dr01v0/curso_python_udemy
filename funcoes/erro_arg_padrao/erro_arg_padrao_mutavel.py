def fibonnaci(sequencia=[0, 1]):
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonnaci()
    print(inicio, id(inicio))
    print(fibonnaci(inicio))
    resetar = fibonnaci()
    print(resetar, id(resetar))
    assert resetar == [0, 1, 1]
