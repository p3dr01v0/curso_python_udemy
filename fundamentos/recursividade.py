# um metodo recursivo chama a si mesmo e necessita de uma condição para a parar de ser executado
def imprimir(maximo, atual):
    if atual < maximo:
        print(atual)
        imprimir(maximo, atual + 1)


imprimir(15, 1)
