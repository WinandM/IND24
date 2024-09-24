nb1 = input("Entrez le premier nombre (entier positif)")
nb2 = input("Entrez le deuxième nombre (entier positif)")
signe = input("Entrez le signe: (+ - * / e ou %)")

#Teste si nb1 ou nb2 contient d'autres caractères que des chiffres
if not nb1.isdigit() or not nb2.isdigit():
    print("Valeurs non conformes")
else:
#converti nb1 et nb2 en chiffre
    nb1 = int(nb1)
    nb2 = int(nb2)
#Effectue le calcul
    if signe == "+":
        print(f"Le résultat est {nb1 + nb2}")
    elif signe == "-":
        print(f"Le résultat est {nb1 - nb2}")
    elif signe == "*":
        print(f"Le résultat est {nb1 * nb2}")
    elif signe == "/":
        print(f"Le résultat est {nb1 / nb2}")
    elif signe == "e":
        print(f"Le résultat est {nb1 ** nb2}")
    elif signe == "%":
        print(f"Le résultat est {nb1 / nb2 * 100}")
#Teste si le signe fait partie des possibilités autorisées
    else:
        print("Valeurs non conformes")   