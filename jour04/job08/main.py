L = [ 8, 24, 27, 48, 2, 16, 9, 7, 84, 91 ]

sum_pairs = 0

for i in L:
    if i % 2 == 0:
        sum_pairs += i

print(sum_pairs)