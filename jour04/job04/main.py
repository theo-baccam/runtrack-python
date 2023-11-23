def func_fruit():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.pop(2)
    fruits.insert(2, "Mangue")
    return fruits

fruit_output = func_fruit()
print(fruit_output)