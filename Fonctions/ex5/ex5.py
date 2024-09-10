def aire_Rect(longueur, largeur):
    return longueur * largeur

def aire_Carre(cote):
    return aire_Rect(cote, cote)

def aire_losange(diag1, diag2):
    return aire_Rect(diag1, diag2)/2

#cette ligne est un troll... ne faites pas ca a la maison.
print(f"l'aire du rectangle est {aire_Rect(float(input("veuillez entrer la longueur du rectangle")), float(input("Veuillez entrer la largeur du rectangle")))}")
