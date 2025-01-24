from sources.score import lireScore, ecrireScore
import random

def jouer():
    #initialisation des règles. la clé indique la valeur, le premier tupple contient les valeurs
    # qui sont battues, le deuxième, celles qui la battent(non utilisés).
    rules = {
        "Pi": [("C", "L"), ("Pa","S")],
        "Pa": [("Pi", "S"),("C","L")],
        "C": [("Pa", "L"), ("Pi","S")],
        "L": [("Pa", "S"), ("Pi","C")],
        "S": [("Pi", "C"), ("Pa", "L")]
    }
    scoreJoueur, scorePC = lireScore()
    print("""Choisissez
    Pi pour pierre
    Pa pour papier
    C pour ciseaux
    L pour Lézard
    S pour Spock""")
    choixJoueur = input("Votre choix? ")
    #vérifie si la valeur éntrée est valide
    if choixJoueur in rules.keys():
        choixPC = random.choice(list(rules.keys()))
        print((f"Le PC choisi {choixPC}"))
        if choixPC == choixJoueur:
            print("Egalité, pas de points distribué")
        else:
            if choixPC in rules[choixJoueur][0]:
                scoreJoueur += 1
                print(f"Le joueur gagne, le score est de {scoreJoueur} pour le joueur et de {scorePC} pour le pc")
            else:
                scorePC += 1
                print(f"Le PC gagne, le score est de {scoreJoueur} pour le joueur et de {scorePC} pour le pc")
            ecrireScore(scoreJoueur, scorePC)
    else:
        print("Choix invalide")
