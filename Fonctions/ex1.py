import math


def perimetreCercle(rayon):
    return 2 * rayon * math.pi


def aireCercle(rayon):
    return math.pi * rayon ** 2


rayon = float(input("Veuillez entrer le rayon: "))
perimetre = perimetreCercle(rayon)
aire = aireCercle(rayon)
print(f"Le périmètre d'un cercle de {rayon} de rayon est {perimetre:.2f} et son aire de {aire:.2f}")
