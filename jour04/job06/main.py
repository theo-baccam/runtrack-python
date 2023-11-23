liste = [ 1, 2, 3, 4, 5 ]

first_value = liste[0]
last_value = liste[-1]
print(liste)

liste.pop(-1)
liste.append(first_value)

liste.pop(0)
liste.insert(0, last_value)

print(liste)