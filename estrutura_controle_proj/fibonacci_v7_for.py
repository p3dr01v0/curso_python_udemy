def fibonacci(quantidade):
    resultado = [0, 1]
    # o uso da "_" no laço for significa uma variavel que não esta sendo usada
    # explicando o range o numero 2 esta presente para a contagem dos itens de resultado começar a partir
    # do segundo valor assim comeca somente depois do 1
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # listar os 20 primerios numeros da sequencia
    for fib in fibonacci(20):
        print(fib)
