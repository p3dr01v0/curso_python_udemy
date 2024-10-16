def tag(tag, *args, **kwargs):
    # print(tag)s
    # print(args)
    # print(kwargs, '\n')
    validos = ('html_class', 'id')
    # a variavel atributos tambem poderia
    atributos = filtro(kwargs, validos)
    conteudo = ''.join(args)
    return f'<{tag} {atributos}>{conteudo}</{tag}>'


def filtro(valores, validador):
    return ''.join(f'{key.split("_")[-1]}="{values}"' for key, values in valores.items() if key in validador)


if __name__ == '__main__':
    print(tag('p',
              tag('span', 'Curso de Python 3, por '),
              tag('strong', 'Juracy Filho', id='jf'),
              tag('span', ' e '),
              tag('strong', 'Leonardo Leitao', id='ll'),
              tag('span', '.'),
              html_class='alert')
          )
