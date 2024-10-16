# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('fim!')

from random import randint

# sorteando um valor aleatorio
def sortear_dado():
    return randint(1, 6)


for x in range(1, 7):
    # vamos trabalahr apenas com numeros pares
    if x %2 == 1:
        continue 
    # verificando se o numero é igual a "x"
    if x == sortear_dado():
        print("ACERTOU, o numero era: ", x)
        break
else:
    print(f"ERROU o numero era: {sortear_dado()}")