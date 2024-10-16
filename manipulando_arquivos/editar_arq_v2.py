# fazendo a leitura atraves do stream, a leitura é feita em trechos, assim não carregando o arquivo inteiro
arquivo = open('manipulando_arquivos/pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}' .format(*registro.split(',')))
arquivo.close()
