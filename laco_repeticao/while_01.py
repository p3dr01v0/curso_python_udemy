#laço infinito
# while True:
#     print("vai demorar muito")

from random import randint

#começamos com o valor de -1 para entrar no laço while, como é um valor aleatorio se a variavel iniciar com 3
# e o 3 for o valor aleatorio escolhi não vamos entrar no laço 
numero_informado = -1
numero_secreto = randint(0, 12)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o numero: '))

print(f'numero secreto {numero_informado} foi encontrado')
