# aqui estamos fazendo uma "fachada", estamos criando um "atalho" para as importações do pacote
# veja que esatmos importando as classes que vamos usar para este arquivo e as colocando na lista
# __all__, objeto que nos permite fazer a "fachada" para nas futuras importações chamarmos somente
# este arquivo ao inves de todos os modulos, podemos ver isso no arquivo "desafio_loja.py"

from .vendedor import Vendedor
from .cliente import Cliente
from .compra import Compra

__all__ = [Cliente, Vendedor, Compra]
