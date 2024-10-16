bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def filtrar_novos_atrs(informados, suportados):
    # aqui esta ocorrendo o seguinte, pegamos o dicionario(**novos_atrs) que foi passado como parametro para a funcao
    # "tag_bloco()", pegamos suas chaves e separamos ela a partir do '_' como por exmeplo: "bloco_id" fica
    # legivel como 'bloco' 'id'.assim possibilitando determinar se o valor do dicionario vai para os atributos
    # da div/span ou para a ul. fazemos o filtro criando duas tuplas e especificando nelas quais valores são permitidos
    # para cada caso, se o valor não for permitido, não será exibido.
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informados.items()
                    if k in suportados)


def tag_bloco(conteudo, *args, classe="sucess", inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'

    # como os atributos estão sendo passados como parte do parametro "conteudo" da funcao tag_bloco tambem passamos
    # o valor do dicionario para a variavel html, assim possibilitando que os atributos cheguem ate a <ul>
    html = conteudo if not callable(conteudo) \
        else conteudo(*args, **novos_atrs)

    # Aqui estamos criando a variavel "atributos" que guarda o valor retornado da funcao de filtro (filtrar_novos_atrs).
    # Passamos a tupla que vai para o parametro de "suportados", que representa os valores permitidos ou não.
    # Além disso passamos o dicionario (novos_atrs) sendo o parametro de "informados".
    atributos = filtrar_novos_atrs(novos_atrs, bloco_atrs)

    return f"<{tag} {atributos} class=\"{classe}\">\n{html}\n</{tag}>"


def tag_lista(*itens, **novos_atrs):
    # aqui fazemos a mesma coisa feita na outra varaivel "atributos", apenas alteramos a tupla que valida os valores
    atributos = filtrar_novos_atrs(novos_atrs, ul_atrs)

    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {atributos}>{lista}</ul>'


if __name__ == '__main__':
    # print(tag_bloco('hello world!'))
    # print(tag_bloco('inline e classe', classe='info', inline=True))
    # print(tag_bloco(conteudo='inline e classe', classe='info', inline=True))
    # print(tag_bloco(conteudo='inline e classe', classe='info'), '\n \n')

    # print(tag_bloco(tag_lista('item 1', 'item 2', 'item 3'), classe='info'), '\n')

    # print(tag_bloco(tag_lista, 'sabado', 'domingo',
    #       classe='info', inline=True), '\n')

    print(tag_bloco(tag_lista, 'item 1', 'item 2', classe='info',
          bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))
