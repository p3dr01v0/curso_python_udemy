palavra = 'palavrajunta'


# como percorre as letras de uma string
for letra in palavra:
    print(letra , end=",")#para o final de cada print ser uma ","


#imprimido uma lista 
aprovados = ['pedro', 'rafaela', 'joao', 'renato', 'ronaldo']

for nomes in aprovados:
    print(nomes)


# lista com os numeros dos indices, fazendo a numeração dos nomes
for posicao, nomes in enumerate(aprovados):
    print(posicao + 1, nomes)# foi colcoado o "+1" para a contagem não iniciar do "0"
    
    
#leitura de tuplas
dias_semana = ('domingo', 'segunda', 'terca', 'quarta', 
               'quinta', 'sexta', 'sabado')

for dias in dias_semana:
    print(f'hoje é dia: {dias}')
    

#leitura sem direta
#ao executar vemos que as letra não estão na ordem
for letra in set('ola mundo'):
    print(f'as letras presentes são {letra}')
    

for numeros in {1,2,3,4,5,6,7,8}:
    print(f'os numeros são {numeros}')