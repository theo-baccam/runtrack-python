def calcule(num1,operator,num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Pas possible.")
            return
    elif operator == '%':
        result = num1 % num2
    else:
        print("Opérateur invalide")
        return

    return result

result = calcule(40,'+',2)
print(result)

result = calcule(7,'-',3)
print(result)

result = calcule(24,'*',7)
print(result)

result = calcule(4,'/',3)
print(result)

result = calcule(0,'/',0)
print(result)

result = calcule(17,'%',5)
print(result)

result = calcule(32,'o',9)
print(result)