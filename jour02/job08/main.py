# Pour vérifier si les longuers données nous permettent de former un triangle
def tri_verif(a,b,c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

# Pour vérifier si le triangle est rectangle ET isocèle.
# Je ne peux pas vraiment tester ceci car, de ce que je comprends, la façon
# dont les floats sont gérés dans Python causent des difficultés, par exemple:
# `10 / 3` donne 3.3333333333333335
def tri_iso_rect(a, b, c):
    if (a == b and a**2 + b**2 == c**2) or \
    (b == c and b**2 + c**2 == a**2) or \
    (c == a and c**2 + a**2 == b**2):
        return True
    else:
        return False

# Vérifie si le triangle est isocèle
def tri_iso(a,b,c):
    if a == b != c or b == c != a or c == a != b:
        return True
    else:
        return False

# Vérifie si le triangle est rectangle via le théorème de Pythagore.
def tri_rect(a,b,c):
    if a**2 == b**2 + c**2 or b**2 == c**2 + a**2 or c**2 == a**2 + b**2:
        return True
    else:
        return False

# Vérifie si un triangle est équilatéral
def tri_equi(a,b,c):
    if a == b == c:
        return True
    else:
        return False

a = float(input('Donnez une longueur a : '))
b = float(input('Donnez une longueur b : '))
c = float(input('Donnez une longueur c : '))

if not tri_verif(a,b,c):
    print('On ne peut pas créer de triangle.')
elif tri_iso_rect(a,b,c):
    print('On peut créer un triangle isocèle et rectangle')
elif tri_iso(a,b,c):
    print('On peut créer un triangle isocèle')
elif tri_rect(a,b,c):
    print('On peut créer un triangle rectangle')
elif tri_equi(a,b,c):
    print('On peut créer un triangle équilatéral.')
else:
    print('On peut créer un triangle quelquonque.')