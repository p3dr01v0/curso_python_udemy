def tipo_dia(dia):
    dias = {
        (1, 7): "final de semana",
        tuple(range(2, 7)): "dia de semana"
    }
    lista = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(lista, '**dia inválido**')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {tipo_dia(dia)}')
