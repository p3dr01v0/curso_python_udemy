class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'estudar', 'falar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'escalar paredes')


class SpiderMan(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('bater em bandidos', 'atirar teia')


if __name__ == '__main__':
    jonh = Homem()
    print(jonh.capacidades)

    aranha = Aranha()
    print(aranha.capacidades)

    peter = SpiderMan()
    print(peter.capacidades)
