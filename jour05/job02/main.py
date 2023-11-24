def rectangle(width, height):
    if width < 2 or height < 2:  # Vérification de dimensions
        raise ValueError("Dimensions trop petites, au moins 2x2")

    # Largeur ajusté pour prendre en compte les bords gauche et droite
    width -= 2

    width_line = "-" * width  # Ligne horizontale pour les bords haut et bas

    width_empty = " " * width  # Vide à l'intérieur du rectangle

    print(f"|{width_line}|")  # Afficher le bord haut
    for i in range(height - 2):  # Afficher lignes vertical avec vides entre eux
        print(f"|{width_empty}|")
    print(f"|{width_line}|")  # Afficher le bord bas


rectangle(2, 2)
rectangle(5, 9)
rectangle(10, 3)
