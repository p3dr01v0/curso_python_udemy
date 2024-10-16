from os import replace


class HtmlToStringMixin:
    def __str__(self):
        html = super().__str__() \
            .replace('(', '<strong>')\
            .replace(')', '</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ""


class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    pessoa_um = Pessoa('Maria')
    print(pessoa_um)

    pessoa_dois = PessoaHtml('Roberto Carlos')
    print(pessoa_dois)

    toto = AnimalHtml('toto')
    print(toto)
