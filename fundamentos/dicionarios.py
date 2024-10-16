#dicionarios são compostos por chaves e seus valores como pode ser visto abaixo
pessoa = {'nome': 'ana', 'idade': 22, 'cursos': ['ingles', 'portugues']}

#é possivel chamar a chave desejada como se fossem indices
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'][0])#especificando o indice 

nova_pessoa = {'nome': 'renato', 'idade': '20', 'cursos': ['react', 'python', 'flutter']}

#modifico o valor da chave idade
nova_pessoa['idade'] = 25

print(nova_pessoa)

#modifico o valor da chave idade eadiciono a chave sexo
nova_pessoa.update({'idade': 40, 'Sexo' : 'M'})

print(nova_pessoa)

#retiro a chave sexo
nova_pessoa.pop('Sexo')

print(nova_pessoa)

#deleto a chave cursos
del nova_pessoa['cursos']

print(nova_pessoa)

#limpo o diconario por completo
nova_pessoa.clear()

print(nova_pessoa)
