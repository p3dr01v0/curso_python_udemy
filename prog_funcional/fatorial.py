def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


if __name__ == '__main__':
    print(f'fatorial de 10: {fatorial(10)}')
