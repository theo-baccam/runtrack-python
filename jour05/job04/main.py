def diagonal_carpet(n):
    x_line = "-" * (n + 1)
    print(f"+{x_line}+")
    val = n
    for i in range(n + 1):
        char = "#" * val
        empt = "#" * (n - val)
        print(f"|{char} {empt}|")
        val -= 1
    print(f"+{x_line}+")

diagonal_carpet(10)