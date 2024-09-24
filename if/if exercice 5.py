import random

PV = 100
continuer = True

while(continuer):
    attaque = random.randint(1, 100)
    if attaque >= 75:
        PV = PV - 75
        print(f"L'attaque a fait 75 dégats")
    elif attaque >= 50 and attaque < 75:
        PV = PV - 75
        print(f"L'attaque a fait 75 dégats")
    else:
        attaque = int( attaque / 2 )
        PV = PV - attaque
        print(f"L'attaque a fait {attaque} dégats")

    if PV <= 0:
        print("Le joueur n'a plus de PV")
        continuer = False
    else:
        print(f"Le joueur a encore {PV} PV")