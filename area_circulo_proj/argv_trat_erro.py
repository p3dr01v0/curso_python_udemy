import math
import sys

pi = 3.14159


#cores
ERRO = '\033[91m'
NORMAL = '\033[0'

def help():
    print('É necessasrio informar o raio do circulo')
    print('Syntaxe: {} <raio>' .format(sys.argv[0][2:]))
    

def calculo(raio):
    return pi * raio ** 2


if __name__ == '__main__':

    if len(sys.argv) > 2:
        help()
        #se cair no laço if o usuario passou argumento errado ou nenhum argumento, assim terminando o programa
        sys.exit(1)
        #erro um valor nulo
        
    elif not sys.argv[1].isnumeric():
        help()
        #erro dois valor invalido
        sys.exit(2)
        #colocando cor no print de erro
        print(ERRO + 'digite um valor numerico' + NORMAL)
        
    else:
        raio = sys.argv[1]
        area = calculo(raio)
        print(f'o valor da área é: {area}')

