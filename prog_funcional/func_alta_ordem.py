from func_primeira_classe import dobro, quadrado


def processar(titulo, alcance, funcao):
    print(f'\nProcessando: {titulo}')
    for i in alcance:
        print(i, '=>', funcao(i))


if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrado de 1 a 10', range(1, 11), dobro)
