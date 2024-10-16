# o codigo presente em try pode ser considerado "perigoso", eles são colocados dentro do try por causa do finally
# o codigo presente no finally é executado mesmo que o codig dotry de erro
try:
    arquivo = open('manipulando_arquivos/pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}' .format(*registro.strip().split(',')))
finally:
    print('arquivo fechado')
    arquivo.close()
