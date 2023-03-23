import numpy as np
b = []

while True:
    a = int(input("Insira um numero para criar uma lista: "))
    b.append(a)
    c = input('Mais algum numero? ')
    if c == 'n':
        break

print(b.max())
print(b.min())
