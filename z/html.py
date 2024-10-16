def filtrar(atributos, validador):
    return ' '.join(f'{key.split("_")[-1]}="{valor}"'for key, valor in atributos.items() if key in validador)


def criar_html(conteudo, *atrs, div_tag=True, **valores_atrs):
    tag_primaria = ('bloco_class', 'bloco_id', 'bloco_style')
    tag = 'div' if div_tag else 'span'
    html = conteudo if not callable(
        conteudo) else conteudo(*atrs, **valores_atrs)
    atributos = filtrar(valores_atrs, tag_primaria)
    return f'<{tag} {atributos}>\n{html}\n</{tag}>'


def lista_ordenada(*valores, **valroes_atrs):
    tag_secundaria = ('ul_class', 'ul_id', 'ul_style')
    lista = ''.join(f'<li>{itens}</li>\n' for itens in valores)
    atributos = filtrar(valroes_atrs, tag_secundaria)
    return f'<ul {atributos}>\n\n{lista}\n</ul>'


if __name__ == '__main__':
    print(criar_html(lista_ordenada, 'item_1', 'item_2', 'item_3',
          div_tag=False, bloco_class="info", bloco_style="bg-dark",
          ul_class="ordenadas", ul_style="bg-blue"))
