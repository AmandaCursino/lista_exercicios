b = []

while True:
    a = int(input("Insira um numero para criar uma lista: "))
    b.append(a)
    c = input('Mais algum numero? ')
    if c == 'n':
        break

lista_ordenada = sorted(b, reverse = True)
print(lista_ordenada)

