def triangle(height):
    l_diag = "/"        # Caractères pour côtés du triangle
    r_diag = "\\"       # Il y a deux backslashes car '\' est un caarctère spécial

    # Pour calculer la marge avant de dessiner
    empty_side = height - 1
    # Pour calculer l'espace à l'intérieur du triangle
    empty_mid = height * 2 - empty_side * 2 - 2

    # Boucle permettant de dessiner le triangle
    for i in range(height):
        # Insérer du vide à côté et à l'intérieur du triangle
        empty_char = " " * empty_side
        empty_char_mid = " " * empty_mid

        # Si on a atteint la base du triangle, changer le caractère de empty_char_mid
        if empty_mid == height * 2 - 2:
            empty_char_mid = "_" * empty_mid

        # Desisiner le triangle
        print(f"{empty_char}{l_diag}{empty_char_mid}{r_diag}")

        # Elargir l'espace à l'intérieur du triangle
        empty_side -= 1
        empty_mid += 2

triangle(5)

## Rajouter boucle si chiffre est négatif.