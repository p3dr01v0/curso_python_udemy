from functools import reduce
from operator import add

alfa = ['z', 'a', 'p', 'b', 'zb', 'za']
valores = [30, 10, 25, 70, 100, 94]
# o sorted não altera o valor, ele simplesmente ordena sem altera o valor
print(sorted(valores), sorted(alfa))
print(valores, alfa)

# altera o valor das listas ao ordenar do menor para o maior e de "A" a "Z"
# valores.sort()
# print(valores)
# alfa.sort()
# print(alfa)

# as funções abaixo funcinam tanto para numeros quanto para letras com exeção do "sum"
print(min(valores))
print(min(alfa))
print(max(valores))
print(max(alfa))
print(sum(valores))
print(reduce(add, valores))
print(reduce(add, alfa))
print(list(reversed(valores)))
print(list(reversed(alfa)))
print(valores, alfa)
