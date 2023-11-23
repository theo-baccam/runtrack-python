from math import prod

L = [ 8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91 ]

prod_interval = [
    i for i in L if 25 <= i <= 90
]

prod_interval = prod(prod_interval)

print(prod_interval)