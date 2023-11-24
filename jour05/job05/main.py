def true_to_caesar(input_msg,shift):
    output_msg = ""
    for char in input_msg:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            output_msg += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            output_msg += char
    print(output_msg)
        

input_str = "The quick brown fox jumped over the lazy dog."
true_to_caesar(input_str,3)