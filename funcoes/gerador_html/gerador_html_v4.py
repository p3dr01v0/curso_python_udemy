def tag_bloco(conteudo, classe="sucess", inline=False):
    # se inline for igual a 'True' a tag vai ser span, caso contrario vai ser div
    tag = 'span' if inline else 'div'
    return f"<{tag} class=\"{classe}\">{conteudo}</{tag}>"


def tag_lista(*itens):
    # para cada item presente na tupla, é criada uma <li> e depois passamos a lista para dentro da <ul>
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


# recebendo os valores em uma tupla, teste fora da aula
tupla_html = input(
    'adicione os valores desejados(use "," para separar os itens): ')


if __name__ == '__main__':
    # passando os paramtros com parametros posicionais e nomeados
    print(tag_bloco('hello world!'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco(conteudo='inline e classe', classe='info', inline=True))
    print(tag_bloco(conteudo='inline e classe', classe='info'), '\n \n')

    # o parametro conteudo é igual a função tag_lista
    print(tag_bloco(tag_lista('item 1', 'item 2', 'item 3'), classe='info'))

    # conteudo fora da aula, teste para ver se funciona assim tambem
    print(tag_bloco(tag_lista(*tupla_html.split(',')), classe='info'))
