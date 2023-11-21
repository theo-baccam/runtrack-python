# Dézoomez pour bien voir l'output entier

import string
alpha = string.ascii_lowercase * 10
alpha_len = len(alpha)

for i in range(0,alpha_len + 1,1):
    if i % 2 != 0:                  # Si c'est impair.
        alpha_step = alpha[0:i]
        print(alpha_step)