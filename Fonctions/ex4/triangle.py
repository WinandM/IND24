import math

def halfPerimeter(a, b, c):
    return (a + b + c)/2

def aire(halfPerimeter, a, b, c):
    return math.sqrt(halfPerimeter * (halfPerimeter - a) * (halfPerimeter - b) * (halfPerimeter - c))

def hauteur(aire, a):
    return (2 * aire) / a
