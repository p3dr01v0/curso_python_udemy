dicionario_proibido = {'politica', 'futebol', 'religiao', 'jogos', 'desenho'}
textos = [
    'vamos discutir sobre politica hoje',
    'vamos falar sobre futebol',
    'voce desenhou muito bem',
    'hoje esta um belo dia para se divertir',
]

for frase in textos:
    #set, fez um conjunto das palavras de "texto" e "textos"
    #intersection, esta funcao esta comparando os conjuntos de palavras de "texto" e "textos" 
    # assim fazendo interseção das palavras comuns(repetidas) entre os dois conjuntos
    barrado = dicionario_proibido.intersection(set(frase.lower().split()))
    if barrado:
        print(f'texto barrado devido a: {barrado}')
    if not barrado:
        print('texto autorizado: ', frase)
