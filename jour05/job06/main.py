def lighthouse(steps, step_height):
    # Calculer le nombre de centimètre parcouru en une semaine, et puis la convertir
    # en mètre.
    weekly = (steps * step_height) * 2 * 7 / 100

    return(
        f"Pour marcher {steps} marches de {step_height}cm, "
        f"le gardien parcourt {weekly}m par semaine."
    )

phare_output = lighthouse(40,7.5)
print(phare_output)