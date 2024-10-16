def tag_bloco(conteudo, *args, classe="sucess", inline=False):
    tag = 'span' if inline else 'div'
    # conteudo pode ser uma simples string como "hello world", caso seja uma string a condicao do if sera verdadeira
    # fazendo com que html seja um astring, caso conteudo seja um objeto que pode ser chamado com parenteses como
    # ex: chamado() html vai ser igual a função conteudo(*args), nesta função ocorre o desempacotamento da tupla args
    # fazendo com que conteudo tenha mais do que um valor
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f"<{tag} class=\"{classe}\">{html}</{tag}>"


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('hello world!'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco(conteudo='inline e classe', classe='info', inline=True))
    print(tag_bloco(conteudo='inline e classe', classe='info'), '\n \n')

    print(tag_bloco(tag_lista('item 1', 'item 2', 'item 3'), classe='info'), '\n')

    # passando o primeiro parametro(conteudo) como um objeto callable(objeto que pode ser chamado), em seguida é
    # passado o segundo parametro(lembrando que o segundo parametro é uma tupla)
    # sabendo o primeiro parametro é um objeto callable a vairavel html vai chamar a funcao conteudo(*args)
    # que faz com o valor de conteudo seja os valores da tupla args
    print(tag_bloco(tag_lista, 'sabado', 'domingo', classe='info', inline=True))
