# o strip retira o caracter desejad
arquivo = open('manipulando_arquivos/pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}' .format(*registro.strip().split(',')))
arquivo.close()
