a = []

while True:
    a.append = input('Entre com um nome para a lista: ')
    c = input('Mais algum nome?(s ou n) ')
    if c == 'n':
        break

x = ""
y = a[0]
z = 0
for i in a:
    if len(i) > len(x):
        x = i
    if len(i) < len(y):
        y = i

print('O maior nome é: ', x)
print('O menor numero é: ', y)