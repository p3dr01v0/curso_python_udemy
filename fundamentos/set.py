numero = set([1,2,3,4,5,6,7,8,9,10])
sub = set([1,3,5,7,9,13,15,16,17])

colecao = numero | sub

intersecao = numero.intersection(sub)

print(colecao)
print(intersecao)
# if intersecao:
#     print('negado: ', intersecao)