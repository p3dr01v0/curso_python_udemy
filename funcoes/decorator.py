def log(function):
    def decorator(*args, ** kwargs):
        print(f"chamando a função: {function.__name__}")
        print(f'args: {args}')
        print(f'args: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'o resultado da função {function.__name__} foi: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 9))
    print(sub(5, y=9))
