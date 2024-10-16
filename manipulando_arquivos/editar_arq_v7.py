import csv

with open('manipulando_arquivos/pessoas.csv') as arquivo:
    for registro in csv.reader(arquivo):
        print('Nome: {}, Idade: {}' .format(*registro))

if arquivo.closed:
    print('arquivos fechados')
