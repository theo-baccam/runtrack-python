# l_empt
# l_diag
# r_diag
# r_empt
# m_empt
# m_line
# middle is height*2 - 2 - empty space

def triangle(height):
    l_diag = "/"
    r_diag = "\\"
    empty_side = height - 1
    empty_mid = height * 2 - empty_side * 2 - 2
    for i in range(height):
        empty_char = " " * empty_side
        empty_char_mid = " " * empty_mid
        if empty_mid == height * 2 - 2:
            empty_char_mid = "_" * empty_mid
        print(f"{empty_char}{l_diag}{empty_char_mid}{r_diag}{empty_char}")
        empty_side -= 1
        empty_mid += 2

triangle(-2)

## Rajouter boucle si chiffre est négatif.