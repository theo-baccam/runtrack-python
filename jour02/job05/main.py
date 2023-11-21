for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:   # Modulo permet de voir si un nombre est divisible
        print('FizzBuzz')           # par un autre.
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)