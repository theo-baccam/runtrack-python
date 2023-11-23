import string

# Faire une list comprehension est plus conscis que faire une boucle for lorsqu'on
# souhaite créer une liste selon des conditions.

def my_long_word(num, input_string):
    words = [
        word.strip(string.punctuation)              # Enlève toute ponctuations
        for word in input_string.split()            # Sépare selon espaces
        if word.strip(string.punctuation)[num:]]    # Si un mot est au dessus de 'num'
    print(words)

input_str = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
my_long_word(3, input_str)