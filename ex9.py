wpp = input('Digite uma lista de números separados por vírgula: ')
wpp = wpp.split(',')
wpp = [int(num) for num in wpp]

for num in wpp:
    if num < 5:
        print(num)