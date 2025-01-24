def gestion_menu():
    print("""1 : Jouer une partie.
2 : Afficher les scores.
3 : Afficher les règles.
4 : Réinitialiser les scores.
5 : Quitter.
""")
    return input("Votre choix? ")

def afficher_regles():
    print("""Les ciseaux coupent le papier,
le papier bat la pierre,
la pierre écrase le lézard,
le lézard empoisonne Spock.
Spock écrabouille les ciseaux,
les ciseaux décapitent le lézard,
le lézard mange le papier,
le papier repousse Spock,
Spock détruit la pierre.
La pierre bat les ciseaux
""")
    input("Retour au menu, press enter")