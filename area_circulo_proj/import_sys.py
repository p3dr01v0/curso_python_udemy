import math
import sys

pi = 3.14159


def calculo(raio):
    return pi * raio ** 2


if __name__ == '__main__':
    #falando que raio é igual ao  segundo argumento que sera passado no cmd an hora de executar o arquivo
    #não é de muita utilidade pois é necessario executar no cmd ou algum outro prompt de comando
    #o uso do input é mais apropriado
    #tratativas de erro
    if len(sys.argv) > 2:
        print('É necessasrio informar o raio do circulo')
        #argv[0] é o primeiro argumento ou seja o nome do arquivo 
        #./aula.py <raio> "./aula.py" é o argv[0], estamos fazendo uso da [2:] para a string imprimir a partir da "/"
        print('Syntaxe: {} <raio>' .format(sys.argv[0][2:]))
    else:
        raio = sys.argv[1]
        area = calculo(raio)
        print(f'o valor da área é: {area}')

