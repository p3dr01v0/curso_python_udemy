palavras_proibidas = ['futebol', 'politica', 'religião']
textos = ['joão gosta de futebol e politica',
          'a praia foi divertida']


#texto esta se referindo as strings que estão na lista textos
for texto in textos:
    found = False
    #lower deixa as palavras em minusculo
    #split pega as palavras a cada espaço em branco, ou seja analisa todas as palvras
    for palavra in texto.lower().split():
        if palavra in palavras_proibidas:
            print('possui uma palavra proibida')
            found = True
            break
    
    if not found:
        print('texto autorizado: ', texto)
        