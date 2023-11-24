def luke_notes(input_list):
    output_list = []
    for i in input_list:
        if i < 0 or i > 100:
            continue
        elif i < 40:
            output_list.append(i)
        else:
            max_count = 0
            for buzz in range(3):
                if (i + buzz) % 5 == 0:
                    output_list.append(i + buzz)
                elif max_count == 2:
                    output_list.append(i)
                max_count += 1
    print(output_list)

notes = [ -2, 101, 39, 42, 83]
luke_notes(notes)