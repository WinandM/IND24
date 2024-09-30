def calculAire(val1, val2):
    return val1 * val2

def printResultat(resultat):
    print(f"l'aire est égale à {resultat}")

valeurAcceptee = ["c", "r", "p", "t"]

while(input("voulez vous calculer une aire? y/n: ").lower() == "y"):
    aireACalculer = input("Quelle aire voulez vous calculer? Carré(c), Rectangle (r), Parallélogramme (p) ou Triangle (t): ").lower()
    if aireACalculer in valeurAcceptee:
        if aireACalculer == valeurAcceptee[0]:
            cote = int(input("Veuillez entrer la valeur d'un coté: "))
            resultat = calculAire(cote, cote)
        elif aireACalculer == valeurAcceptee[1]:
            largeur = int(input("Veuillez entrer la valeur de la largeur: "))
            longueur = int(input("Veuillez entrer la valeur de la longueur: "))
            resultat = calculAire(longueur, largeur)
        else:
            base = int(input("Veuillez entrer la valeur de la base: "))
            hauteur = int(input("Veuillez entrer la valeur de la hauteur: "))
            resultat = calculAire(base, hauteur)
            if aireACalculer  == valeurAcceptee[3]:
                resultat /= 2
        printResultat(resultat)
    else:
        print("Valeur non acceptée")
