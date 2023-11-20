# On utilise une variable de type dictionaire contient plusieurs attributs de
# type différents, utile pour la gestion de données.
produit = {
    'nom': 'produit 1',
    'prix': 2,
    'quantite': 35
}

# `\n` sert à sauter la ligne.
# on sépare des éléments avec une virgule.
print("Nom:", produit['nom'], 
"\nPrix:", produit['prix'],
"\nQuantité:", produit['quantite'])

quantite_achat=input("Quelle est la quantité que vous souhaitez achetez? ")
print("Cela vous côutera",2 * int(quantite_achat),"€")
print("")

# `-=` permet de soustraire une valeur, et puis l'attribuer directement.
# Plus simple que valeur1 = valeur1 - valeur2
produit['quantite'] -= int(quantite_achat)
print("Suite à l'achat",
"\nNom:", produit['nom'], 
"\nPrix:", produit['prix'],
"\nQuantité:", produit['quantite'])
print("")

# `*=` est similaire à `-=`, mais pour la multiplication.
produit['prix'] *= 1.1
print("Suite à une hausse de prix de 10%",
"\nNom:", produit['nom'], 
"\nPrix:", produit['prix'],
"\nQuantité:", produit['quantite'])