from sources.menu import gestion_menu, afficher_regles
from sources.jeu import jouer
from sources.score import lireScore, reinitialiserScore

continuer = True
while continuer:
    choixMenu = gestion_menu()
    if choixMenu == "1":
        jouer()
    elif choixMenu == "2":
        scoreJoueur, scorePC = lireScore()
        print(f"Le score du joueur est {scoreJoueur}, le score du PC {scorePC}")
    elif choixMenu == "3":
        afficher_regles()
    elif choixMenu == "4":
        reinitialiserScore()
        print("Score réinitialisé")
    elif choixMenu == "5":
        print("Merci d'avoir joué!")
        continuer = False
    else:
        print("Choix invalide!")
