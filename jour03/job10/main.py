def even_odd(num):
    if num < 0 or num % 1 != 0:
        print("Nombre invalide")
    elif num % 2 == 0:
        print("pair")
    else:
        print("impair")

even_odd(0.5)
even_odd(-25)
even_odd(2)
even_odd(5)