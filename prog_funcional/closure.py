def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    # ao declararmos as variaveis passamos o prametro "x" da função multipliacar
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    quadruplo = multiplicar(4)

    # ao executar os print abixos temos 'multiplicar.<locals>.calcular' o que indica que a função sabe onde foi
    # declarada e sabe o que esta ao seu redor, por causa disso ela tem o valor do parametro "x"
    print(dobro)
    print(triplo)
    print(quadruplo)

    # desta vez  estamos passando o parametro da função calcular, o parametro "y"
    print(f'{dobro(5)}')
    print(f'{triplo(5)}')
    print(f'{quadruplo(5)}')
