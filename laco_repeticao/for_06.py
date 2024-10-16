palavras_proibidas = ['futebol', 'politica', 'religião']
textos = ['joão gosta de futebol e politica',
          'a praia foi divertida']


for texto in textos:
    for palavra in texto.lower().split():
        if palavra in palavras_proibidas:
            print('possui uma palavra proibida: ', palavra)
            break
else:
    print('texto autorizado: ', texto)
        