string = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

def my_long_word(num, input_string):
    word_start = 0
    word_end = 1
    current_word = ""
    current_word_length = 0
    output = []
    for index, char in enumerate(input_string):
        if (char == " " or char == ", ") and current_word_length > num:
            current_word = input_string[word_start:word_end]
            print(current_word_length)
            output.append(current_word)
            word_start = index + 1
            current_word_length = 0
        elif char.isalpha() or char == "'":
            word_end = index + 1
            current_word_length += 1
        else:
            word_start = index + 1
            current_word = ""
            current_word_length = 0
    current_word = input_string[word_start:word_end]
    output.append(current_word)
    print(output)

my_long_word(3, string)