lista = [1, 2, 3]

dobro = map(lambda x: x * 2, lista)

print(list(dobro))

nome_idade = (
    {'nome': 'pedro', 'idade': 23},
    {'nome': 'maria', 'idade': 31},
    {'nome': 'joao', 'idade': 19}
)

so_nomes = map(lambda n: n['nome'], nome_idade)
so_idade = map(lambda n: n['idade'], nome_idade)

print(tuple(so_nomes))
print(tuple(so_idade))
print(sum(list(so_idade)))

frase = map(lambda fra: f'{fra["nome"]} tem {fra["idade"]} anos', nome_idade)
print(tuple(frase))
