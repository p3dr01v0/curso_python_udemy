class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def is_adulto(self):
        return self.idade > 18

    def __str__(self):
        return f'{self.nome} ({self.idade} anos)'
