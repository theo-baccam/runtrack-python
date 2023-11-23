L = [ 8, 24, 27, 48, 2, 16, 9, 7, 84, 91 ]

sum_pairs = 0

for i in range(len(L)):
    if L[i] % 2 == 0:
        sum_pairs += L[i]

print(sum_pairs)