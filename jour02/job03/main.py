# Pas besoin de définir `i` dans une boucle `for`.

for i in range(101):        # range spécifie qu'on va jusqu'à 100 (101 pas inclus)
    if i in {26, 37, 88}:   # si i est égale à ces nombres...
        continue            # on revient au début de la boucle
    print(i)