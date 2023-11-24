def true_to_caesar(input_msg, shift):
    output_msg = ""

    for char in input_msg:
        # Si le caractère est une lettre de l'alphabet, faire un décalage
        if char.isalpha():
            # ord() permet d'obtenir l'unicode d'un caractère
            offset = ord("A") if char.isupper() else ord("a")

            # Décalage
            # Modulo 26 permet de revenir à 0 au cas où on sort de l'alphabet.
            # Par exemple si on est à Z est qu'on décale de 1, on va à A, et pas
            # sur un symbole spécial.
            output_msg += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Si ce n'est pas une lettre de l'alphabet, pas besoin de la décaler.
            output_msg += char

    return output_msg


input_str = "The quick brown fox jumped over the lazy dog."
tqbf_output = true_to_caesar(input_str, 3)
print(tqbf_output)
