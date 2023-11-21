n = input('Entrez un entier supérieur à zero (N) : ')
multi = 1

for i in range(1, int(n) + 1):
    print('Table de multiplication de', i, ':')
    for multi in range(1, 11):
        print(i, 'x', multi, '=', i * multi)
    print('')