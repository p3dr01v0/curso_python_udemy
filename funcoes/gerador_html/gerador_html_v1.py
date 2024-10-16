def tag_bloco(texto, classe="sucess"):
    return f"<div class=\"{classe}\">{texto}</div>"


if __name__ == '__main__':
    assert tag_bloco('Incluído com sucesso!') == \
        '<div class="sucess">Incluído com sucesso!</div>'
    assert tag_bloco('Impossivel excluir!', 'error') == \
        '<div class="error">Impossivel excluir!</div>'

    print(tag_bloco(texto='hello world!'))
