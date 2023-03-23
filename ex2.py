b = []

while True:
    a = input("Insira uma palavra para criar uma lista: ")
    b.append(a)
    c = input('Mais alguma palavra?(s ou n) ')
    if c == 'n':
        break

d = []
for i in b:
    if i[0] == 'a':
        d.append(i)
print(d)