# MONTANT INITIAL DE L'INVESTISSEMENT:
# Le capital de départ que l'investisseur met, la somme initiale.

# TAUX DE RENDEMENT ANNUEL
# Le pourcentage du gain ou de la perte sur l'investissement.

montant_initial = 4000
rendement_annuel = 102

print("2024:", montant_initial * rendement_annuel / 100)

montant_initial += 5000
rendement_annuel += 2
print("2025:", montant_initial * rendement_annuel / 100)

montant_initial *= 0.9
rendement_annuel -= 1
print("2026:", montant_initial * rendement_annuel / 100)
