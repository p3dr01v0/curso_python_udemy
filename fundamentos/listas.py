lista = [6,7,8,9,10]

#é possivel misturar os tipos em uma lista, não recomendado devido a organização
# lista_mista = [11,12,13,'fulano', 'cicrano']
# print(lista_mista)

#imprimindo indice especifico
print(lista[3])

print(lista)

#removendo o valor não o indice
lista.remove(7)

print(lista)

#adicionando valor a lista 
lista.append(7)

print(lista)

lista_deletada = [21,22,23,24,25,26,27,28,29,30]

print(lista_deletada[:1])#imprimi o indice especificado
print(lista_deletada[:-3])#imprimi todos os indices menos os indices seguintes após o que foi especificado
print(lista_deletada[::3])#imprimi em intervalos de 3 indices

del lista_deletada[9] #deleta o indice especificado
print(lista_deletada)

del lista_deletada[4:] #deleta o indice especificado adiante
print(lista_deletada)

lista_novo = [15,16,17]

lista_novo[0] = 60

print(lista_novo)
