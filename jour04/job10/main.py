L = [ 8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91 ]

sum_interval = 0
for i in L:
    if 25 <= i <= 90:
        sum_interval += i

print(sum_interval)