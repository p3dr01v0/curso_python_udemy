compras = (
    {'quantidade': 5, 'valor': 30},
    {'quantidade': 10, 'valor': 40},
    {'quantidade': 15, 'valor': 50}
)

total = tuple(
    map(lambda compra: compra['quantidade'] * compra['valor'], compras)
)

print(total)
print(f'total: {sum(total)}')
