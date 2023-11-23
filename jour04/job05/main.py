def replace():
    new_value = L[2] + L[4]
    L.pop(3)
    L.insert(3, new_value)
    print(L)

L = [ 5, 9, 18, 82, 37]

print(L)
print(L[2])

replace()
print(L[-1])