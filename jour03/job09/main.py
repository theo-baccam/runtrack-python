def moyenne(a,b,c):
    moyenne_etudiant = (int(a)+int(b)+int(c))/3
    if 20 >= moyenne_etudiant >= 15:
        print("Très bon élève")
    elif 14 >= moyenne_etudiant >= 11:
        print("Bon élève")
    elif 10 >= moyenne_etudiant >= 8:
        print("Elève moyen")
    elif 7 >= moyenne_etudiant >= 0:
        print("Elève devant faire des efforts")

note1 = input("Donnez une première note :")
note2 = input("Donnez une deuxième note :")
note3 = input("Donnez une troisième note :")

moyenne(note1,note2,note3)
    