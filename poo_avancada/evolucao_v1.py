class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        # quando uma instancia retorna self é possivel fazer chamadas em cadeiamento como na linha 16
        return self


if __name__ == '__main__':
    jose = Humano('jose')
    grokn = Humano('grok').das_cavernas()

    print(f'Humano.especie {Humano.especie}')
    print(f'jose.especie {jose.especie}')
    print(f'grokn.especie {grokn.especie}')
