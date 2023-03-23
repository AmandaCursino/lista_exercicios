b = []

while True:
    a = int(input("Insira um numero para criar uma lista: "))
    b.append(a)
    c = input('Mais algum numero? ')
    if c == 'n':
        break

d = []
for i in b:
    if i%2 == 0:
        d.append(i)
print(d)