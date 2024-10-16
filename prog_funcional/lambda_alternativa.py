compras = (
    {'quantidade': 5, 'valor': 30},
    {'quantidade': 10, 'valor': 40},
    {'quantidade': 15, 'valor': 50}
)


def preco_total(compra):
    return compra['quantidade'] * compra['valor']


total = tuple(
    map(preco_total(), compras)
)

print(total)
print(f'total: {sum(total)}')
