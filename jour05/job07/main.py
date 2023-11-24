def luke_notes(input_list):
    output_list = []

    # On utilise une list comprehension car c'est plus court qu'une boucle for.
    # Si un nombre dans liste est en dessous de 40, la mettre dans la liste output
    # tel quel.
    output_list = [
        # Si il y un nombre à un multiple de 5 existe à moins de 3 points au dessous,
        # arrondir la note à ça. Sinon rendre la note tel quel.
        i if i < 40 else i + (5 - i % 5) if i % 5 > 2 else i
        for i in input_list
        if 0 < i < 100  # Si c'est en dessous de 0 ou dessus de 100, ignorer
    ]
    return output_list


notes = [-2, 101, 39, 42, 83]
resultats = luke_notes(notes)
print(resultats)
