def replace(list_name):
    new_value = list_name[2] + list_name[4]
    list_name.pop(3)
    list_name.insert(3, new_value)

L = [ 5, 9, 18, 82, 37]

print(L)
print(L[1])

replace(L)
print(L)
print(L[-1])