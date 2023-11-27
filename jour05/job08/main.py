# L'algorithme qu'on utilise s'apelle le "Bubble Sort"

def my_sort(input_list):
    # Dans le pire cas, ça prendra "n - 1" d'itérations pour ranger une liste avec bubble sort.
    # (n est le nombre d'élément dans une liste)

    for iteration in range(len(input_list)):
        # Liste à part, si on opère directement sur la liste durant une boucle for, les index changent.
        mod_list = []
        # Pour déterminer si un échange s'est passé.
        is_sorted = True
        # Valeur de l'élément précédent.
        last_value = None
        # Faut mettre les valeurs par défaut au début de la boucle, sinon boucle infinie

        # La boucle pour échanger les places
        for index, value in enumerate(input_list):
            # Si c'est pas index 0 et valeur du nombre est plus petite que le précédent.
            if last_value is not None and value < last_value:
                # Insérer le nombre de en arrière.
                mod_list.insert(index - 1, value)
                # Signaler que la liste est en désordre.
                is_sorted = False
            else:
                # Insérer le nombre normalement
                mod_list.insert(index, value)
            # Changer la dernière valeur pour la prochaine itération de cette boucle.
            last_value = value
        # Appliquer les changements à la liste pour la prochaine itération de la boucle
        input_list = mod_list

        # Si la liste est bien en ordre, terminer la fonction.
        if is_sorted:
            return (
                f"Nombre total de coups nécessaires pour trier la liste: {iteration}"
                f"\nListe triée: {input_list}"
            )


list_1 = [23, 74, 90, 212, 589]
out_1 = my_sort(list_1)
print(out_1)

list_2 = [239, 190, 104, 63, 21]
out_2 = my_sort(list_2)
print(out_2)

list_3 = [92, 19, 5, 547, 219]
out_3 = my_sort(list_3)
print(out_3)

list_4 = [42, 17, 8, 99, 23, 56, 4, 71, 12, 33, 88, 19, 62, 37, 50, 77, 29, 91, 6, 45]
out_4 = my_sort(list_4)
print(out_4)
