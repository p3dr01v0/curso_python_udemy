pessoas = [
    {'nome': 'Pedro', 'idade': 12},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Helena', 'idade': 6},
    {'nome': 'Cleiton', 'idade': 19},
    {'nome': 'Beatriz', 'idade': 17},
]

menor_idade = filter(lambda m: m['idade'] < 18, pessoas)
tamanho_nome = filter(lambda n: len(n['nome']) > 6, pessoas)

# caso fosse o map seria retornado apenas True e False
# menor_idade = map(lambda m: m['idade'] > 18, pessoas)
# tamanho_nome = map(lambda n: len(n['nome']) >= 7, pessoas)

print(tuple(menor_idade))
print(tuple(tamanho_nome))
