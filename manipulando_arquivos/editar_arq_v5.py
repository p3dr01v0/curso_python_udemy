# o bloco with fecha o arquivo sozinho tornando o codigo mais seguro
with open('manipulando_arquivos/pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}' .format(*registro.strip().split(',')))

if arquivo.closed:
    print('arquivo fechado')
