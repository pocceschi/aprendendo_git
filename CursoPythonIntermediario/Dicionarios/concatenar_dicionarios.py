# para concatenar dicionarios (somar) usar a função update

d1 = {
    1: 2,
    3: 4,
    5: 6,
    7: 8,
}

print(d1)
print()

d2 = {
    "a": "x",
    "b": "y",
}

d1.update(d2)
print(d1)
