L = [ 8, 24, 48, 2, 16]
fizz = 0

for i in range(len(L)):
    if L[i] % 3 == 0:
        fizz += 1

print(fizz)