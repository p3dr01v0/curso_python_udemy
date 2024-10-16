class Compra:
    def __init__(self, vendedor, item, data, valor):
        self.item = item
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

    def __str__(self):
        return f'\nVendedor: {self.vendedor}; item: {self.item}, data: {self.data}, valor: {self.valor}'
