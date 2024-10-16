# versão comprehension
dobro_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobro_pares)

# vesão normal
normal = []

for i in range(10):
    if i % 2 == 0:
        normal.append(i * 2)
print(normal)
