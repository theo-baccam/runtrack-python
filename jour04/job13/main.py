doublon = [10,20,30,20,10,50,60,40,80,50,40]

no_doublon = []

for i in doublon:
    if i not in no_doublon:
        no_doublon.append(i)

print(no_doublon)