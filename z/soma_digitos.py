def soma_digitos_valor():
    soma = 0
    i = 0
    valor = input("Digite um valor: ")

    while i < len(valor):
        soma += int(valor[i])
        i += 1
    return f'A soma dos digitos presentes eh: {soma}'


if __name__ == '__main__':
    print(soma_digitos_valor())
