def media_numeros_pares(limite):
    numeros = []
    i = 0

    while i <= limite:
        if i % 2 == 0:
            numeros.append(i)
            soma = sum(numeros)
        i += 1

    media = soma / i

    return print(f'A media dos numeros pares de 0 a 100 eh: {round(media, 2)}')


if __name__ == '__main__':
    media_numeros_pares(100)
