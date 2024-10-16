# with open('manipulando_arquivos/pessoas.csv') as arquivo:
#     for registro in arquivo:
#         formatado = registro.strip().split(',')
#         lista = formatado[1], formatado[3]
#         print('quarto campo: {}, nono campo:{}' .format(*lista))

def desafio_ibge():
    with open('manipulando_arquivos/desafio_ibge.csv') as arquivo:
        for registro in arquivo:
            formatado = registro.strip().split(',')
            lista = formatado[8], formatado[3]
            print('{} {}' .format(*lista))


desafio_ibge()
