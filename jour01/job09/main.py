produit = {
    'nom': 'produit 1',
    'prix': 2,
    'quantite': 35
}

print("Nom:", produit['nom'], 
"\nPrix:", produit['prix'],
"\nQuantité:", produit['quantite'])

quantite_achat=input("Quelle est la quantité que vous souhaitez achetez? ")
print("Cela vous côutera",2 * int(quantite_achat),"€")
print("")
produit['quantite'] = produit['quantite'] - int(quantite_achat)
print("Suite à l'achat",
"\nNom:", produit['nom'], 
"\nPrix:", produit['prix'],
"\nQuantité:", produit['quantite'])
print("")

produit['prix'] = produit['prix'] * (( 110 / 100 ))
print("Suite à une hausse de prix de 10%",
"\nNom:", produit['nom'], 
"\nPrix:", produit['prix'],
"\nQuantité:", produit['quantite'])