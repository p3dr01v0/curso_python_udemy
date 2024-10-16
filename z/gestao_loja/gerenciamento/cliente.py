from .pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registar_compra(self, compra):
        self.compras.append(compra)

    def get_ultima_data(self):
        return None if not self.compras else \
            sorted(self.compras, key=lambda c: c.data)[-1].data

    def total(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total

    def relatar_compra(self):
        return f'{" ".join(str(compra) for compra in self.compras)}'

    def __str__(self):
        return super().__str__() + ' (adulto)' if self.is_adulto() else ""
