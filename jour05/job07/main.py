def luke_notes(input_list):
    output_list = []
    output_list = [
        i if i < 40 else i + (5 - i % 5) if i % 5 > 2 else i
        for i in input_list
        if 0 < i < 100
    ]
    print(output_list)

notes = [ -2, 101, 39, 42, 83]
luke_notes(notes)