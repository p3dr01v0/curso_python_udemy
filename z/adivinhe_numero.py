from random import randint


while True:
    numero = int(input('numero: '))
    numero_sorteado = randint(1,5)
    if numero != numero_sorteado:
        print('ERROU o numero era: ', numero_sorteado)
    elif numero == numero_sorteado:
        print('ACERTOU era: ', numero_sorteado)
        break
