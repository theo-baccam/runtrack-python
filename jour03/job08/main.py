def mm_food(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    if type == "fruits" and saison == "ete":
        print("poire,fraise,cassis")
    if type == "legume" and saison == "hiver":
        print("carotte,topinambour, endive")
    if type == "legume" and saison == "ete":
        print("artichaut, aubergine,navet")

mm_food("fruits","hiver")
mm_food("fruits","ete")
mm_food("legume","hiver")
mm_food("legume","ete")