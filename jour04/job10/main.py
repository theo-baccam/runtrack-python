L = [ 8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91 ]

prod_interval = 1
for i in L:
    if 25 <= i <= 90:
        prod_interval *= i

print(prod_interval)