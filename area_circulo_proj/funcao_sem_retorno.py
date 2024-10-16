import math

pi = 3.14159


#criando função com precisando do parametro raio para ser executada
def calculo(raio):
    print('Área do circulo: ', pi * raio ** 2)


#executa o codigo caso o nome do modulo seja __main__
if __name__ == '__main__':
    diametro = float(input("Digite o valor do diâmetro: "))
    raio = diametro / 2
    calculo(raio)


#caso o programa esteja encerrando automaticamente
# end = input("executar programa")
