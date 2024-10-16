from datetime import datetime
from loja import Vendedor, Cliente, Compra


def main():
    cliente = Cliente("Maria", 45)
    vendedor = Vendedor("Luan", 32, 5200)
    compra1 = Compra(vendedor, datetime.now(), 530)
    compra2 = Compra(vendedor, datetime(2019, 6, 12), 213)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)

    print(f"Clinte: {cliente}", '(adulto)' if cliente.is_adulto() else "")
    print(f"Vendedor: {vendedor}")

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)

    print(f"Total: {valor_total} em {qtde_compras} compras")
    print(f"Ultima compra {cliente.get_data_ultima_compra()}")


if __name__ == '__main__':
    main()
