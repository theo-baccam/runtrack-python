def dev_type(langage):
    langage = langage.lower()   # Afin que ça soit case-insensitive
    if langage == "javascript":
        print("tu es un développeur web")
    elif langage == "python":
        print("tu es un développeur IA")
    elif langage == "java":
        print("tu es un développeur logiciel")
    elif langage == "reactjs":
        print("tu es un développeur mobile")
    else:
        print("un jour, je serai le meilleur de développeur...")
    
dev_type("JavaScript")
dev_type("pytHon")
dev_type("java")
dev_type("reactjs")
dev_type("uhhhh")