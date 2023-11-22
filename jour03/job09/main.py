def moyenne(a,b,c):
    moyenne_etudiant = (int(a)+int(b)+int(c))/3
    if moyenne_etudiant < 20 and moyenne_etudiant > 15:
        print("Très bon élève")
    elif moyenne_etudiant < 14 and moyenne_etudiant > 11:
        print("Bon élève")
    elif moyenne_etudiant < 10 and moyenne_etudiant > 8:
        print("Elève moyen")
    elif moyenne_etudiant < 7 and moyenne_etudiant > 0:
        print("Elève devant faire des efforts")

note1 = input("Donnez une première note :")
note2 = input("Donnez une deuxième note :")
note3 = input("Donnez une troisième note :")

moyenne(note1,note2,note3)
    