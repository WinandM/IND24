import triangle

a = float(input("Veuillez entrer le coté a: "))
b = float(input("Veuillez entrer le coté b: "))
c = float(input("Veuillez entrer le coté c: "))

halfPerimeter = triangle.halfPerimeter(a, b, c)
aire = triangle.aire(halfPerimeter, a, b, c)
hauteur = triangle.hauteur(aire, a)

print(f"pour un triangle de coté {a}, {b} et {c}, l'aire est {aire} et la hauteur pour le coté a {hauteur}")
