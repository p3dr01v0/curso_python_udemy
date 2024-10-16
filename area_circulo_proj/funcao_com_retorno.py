import math

pi = 3.14159


#criando função com precisando do parametro raio para ser executada
#função retorna a formula, pode ser utilizada para calcular a area de um circulo
def calculo(raio):
    return pi * raio ** 2


#executa o codigo caso o nome do modulo seja __main__
if __name__ == '__main__':
    diametro = float(input("Digite o valor do diâmetro: "))
    raio = diametro / 2
    area = calculo(raio)
    print(f'o valor da área é: {area}')


#caso o programa esteja encerrando automaticamente
# end = input("executar programa")
