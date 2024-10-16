from datetime import datetime

from gerenciamento import Vendedor, Compra, Cliente


def main():
    cliente = Cliente('Helena', 33)
    vendedor = Vendedor('Marcio', 42, 'R$4.300,00')
    compra_um = Compra(vendedor, 'mochila', datetime.now(), 320)
    compra_dois = Compra(vendedor, 'blusa', datetime(2021, 9, 17), 180)

    cliente.registar_compra(compra_um)
    cliente.registar_compra(compra_dois)

    total = cliente.total()
    recente = cliente.get_ultima_data()
    relatorio = cliente.relatar_compra()

    print(f'Cliente: {cliente}')
    print(f'Vendedor: {vendedor}')
    print(f'Valor total gasto: R${total},',
          f'total de compras {len(cliente.compras)}')
    print(f'Ultima compra: {recente}')
    print(f'\nRelatorio das compras: {relatorio}')


if __name__ == '__main__':
    main()
