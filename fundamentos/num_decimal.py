from decimal import Decimal, getcontext

a = Decimal(2) / Decimal(8)

getcontext().prec = 4
print(a)

# b = 1/7

# print(b)
# print(type(b))
# print(type(a))
