def rectangle(width, height):
    if width < 2 or height < 2:
        raise ValueError("Dimensiosn trop petites, au moins 2x2")
    width -= 2
    x_line = "-" * width
    x_empty = " " * width
    print(f'|{x_line}|')
    for i in range(height - 2):
        print(f'|{x_empty}|')
    print(f'|{x_line}|')

rectangle(2,2)
rectangle(5,9)
rectangle(10,3)