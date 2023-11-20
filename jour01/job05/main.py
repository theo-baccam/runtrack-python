import string

# Nous créeons ue nouvelle variable et nous utilisons découpage.
# Le format pour le découpage est `[start:stop:step]`
# Dans ce cas là, on laisse tout vide, à part le step, qu'on met à nombre négatif,
# ce qui permet de lire le string à l'envers.
abc_inv = string.ascii_lowercase[::-1]
print(abc_inv)