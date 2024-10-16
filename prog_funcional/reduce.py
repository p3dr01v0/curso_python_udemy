from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 12},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Helena', 'idade': 6},
    {'nome': 'Cleiton', 'idade': 19},
    {'nome': 'Beatriz', 'idade': 17},
]


so_idade = map(lambda p: p['idade'], pessoas)
menor_idade = filter(lambda idade: idade < 18, so_idade)
soma_menor_idade = reduce(lambda idades, p: idades + p, menor_idade, 0)
print(soma_menor_idade)

# irei fazer duas vezes a mesma  variavel para poder reutilizar ela, como se trata de um objeto map, ao utiliza-lo
# uma vez não é possivel reutiliza-lo novemente, se executar o codigo abaixo sem declarar novamente, o retorno será 0
so_idade = map(lambda p: p['idade'], pessoas)
soma_idade = reduce(lambda idades, p: idades + p, so_idade, 0)
print(soma_idade)
