def diagonal_carpet(n):
    if n <= 0:
        raise ValueError("Taille invalide, doit être au dessus de 0")
    # Bord pour le haut et le bas, n + 1 afin que la diagonale va correctement d'un
    # coin à l'autre.
    border_line = "-" * (n + 1)

    # Dessiner le bord haut
    print(f"+{border_line}+")

    # Le nombre de caractère avant de laisser un espace vide
    val = n

    # n + 1 car range() ne marche pas inclusivement, c'est à dire que si on met
    # range(100), ça va aller jusqu'à 99, pas 100
    for i in range(n + 1):
        left = "#" * val
        right = "#" * (n - val)

        # Dessiner le bord bas
        print(f"|{left} {right}|")

        # Réduire le nombre de caractère à dessiner pour le partie gauche.
        val -= 1

    print(f"+{border_line}+")


diagonal_carpet(10)
