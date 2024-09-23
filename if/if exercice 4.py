saison = input("Entrez une saison: H(hiver), P(printemps), E(été) ou A(automne)? ").lower()

if saison == "h":
    print("récoltez du bois")
elif saison == "p":
    print("récoltez des fleurs")
elif saison == "e":
    print("récoltez des fruits")
elif saison == "a":
    print("récoltez des champignons")
else:
    print("Vous avez introduit une mauvaise valeur")
