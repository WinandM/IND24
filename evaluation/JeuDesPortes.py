import random

rejouer = True
nbJoue = 0
nbGagneChange = 0
nbGagne = 0

while rejouer:
    nbJoue += 1
    porteGagnante = random.randint(1, 3)
    porteChoix = int(input("Quelle porte choisissez vous? 1, 2 ou 3? "))
    if porteChoix == porteGagnante:
        if porteChoix == 1:
            porteOuverte = 2
        else:
            porteOuverte = 1
    else:
        if porteChoix + porteGagnante == 3:
            porteOuverte = 3
        elif porteChoix + porteGagnante == 4:
            porteOuverte = 2
        else:
            porteOuverte = 1
    changer = input(f"vous avez choisi la porte {porteChoix}, le MJ a ouvert la porte {porteOuverte} qui était vide, voulez vous changer votre choix? o/n: ").lower()
    if changer == 'o' and porteChoix != porteGagnante:
        print("Bon choix, il fallait changer")
        nbGagne += 1
        nbGagneChange += 1
    elif changer == 'n' and porteChoix == porteGagnante:
        print("Bon choix, il faut toujours faire confiance a sa première intuition")
        nbGagne += 1
    else:
        print("perdu. le changement c'est la vie")
    print(f"Vous avez joué {nbJoue} parties, vous avez gagné {nbGagne} fois dont {nbGagneChange} en changeant votre avis")

    if input("veux tu recommencer? o/n: ") == "n":
        rejouer = False