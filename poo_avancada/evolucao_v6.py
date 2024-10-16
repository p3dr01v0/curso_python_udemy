from abc import ABCMeta, abstractmethod, abstractproperty


class Humano(metaclass=ABCMeta):
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @abstractproperty
    def inteligente(self):
        pass

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError(f'A idade deve ser maior do que 0')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australoptecos',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':

    # try:
    #     anonimo = Humano('John Doe')
    #     print(anonimo.inteligente)
    # except TypeError:
    #     print(f'classe abstrata')

    jose = HomoSapiens('jose')
    grokn = Neanderthal('grokn')

    print(
        f'jose (da classe {jose.__class__.__name__}) inteligente? {jose.inteligente}')

    print(f'gronk (da classe {grokn.__class__.__name__})',
          f'inteligente? {grokn.inteligente}')
