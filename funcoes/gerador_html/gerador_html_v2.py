def tag_bloco(texto, classe="sucess", inline=False):
    # se inline for igual a 'True' a tag vai ser span, caso contrario vai ser div
    tag = 'span' if inline else 'div'
    return f"<{tag} class=\"{classe}\">{texto}</{tag}>"


if __name__ == '__main__':
    print(tag_bloco('hello world!'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco(texto='inline e classe', classe='info', inline=True))
    print(tag_bloco(texto='inline e classe', classe='info'))
