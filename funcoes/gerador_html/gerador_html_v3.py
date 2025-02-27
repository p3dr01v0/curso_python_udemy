def tag_bloco(conteudo, classe="sucess", inline=False):
    # se inline for igual a 'True' a tag vai ser span, caso contrario vai ser div
    tag = 'span' if inline else 'div'
    return f"<{tag} class=\"{classe}\">{conteudo}</{tag}>"


def tag_lista(*itens):
    # para cada item presente na tupla, é criada uma <li> e depois passamos a lista para dentro da <ul>
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    # passando os paramtros com parametros posicionais e nomeados
    print(tag_bloco('hello world!'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco(conteudo='inline e classe', classe='info', inline=True))
    print(tag_bloco(conteudo='inline e classe', classe='info'), '\n \n')

    # o parametro conteudo é igual a função tag_lista
    print(tag_bloco(tag_lista('item 1', 'item 2', 'item3'), classe='info'))
