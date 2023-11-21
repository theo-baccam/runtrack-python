i = 0

for i in range(101):        # range spécifie qu'on va jusqu'à 100 (101 pas inclus)
    if i in {26, 37, 88}:   # si i est égale à ses nombres...
        continue            # revient au début de la boucle
    print(i)