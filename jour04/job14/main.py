import string

def my_long_word(num, input_string):
    words = [
        word.strip(string.punctuation) 
        for word in input_string.split() 
        if word.strip(string.punctuation)[num:]]
    print(words)

input_str = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
my_long_word(3, input_str)