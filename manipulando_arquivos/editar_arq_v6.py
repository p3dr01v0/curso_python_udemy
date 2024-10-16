# esta sendo criado um arquivo txt como saida, o termo "w" no segundo bloco with na abertura de um arquivo txt
# faz com que seja possivel editar o arquivo que esta sendo especificado anteriormente
with open('manipulando_arquivos/pessoas.csv') as arquivo:
    with open('manipulando_arquivos/pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}' .format(*pessoa), file=saida)

if arquivo.closed and saida.closed:
    print('arquivos fechados')
