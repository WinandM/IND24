
def lireScore():
    try:
        fichier = open("score/score.txt", "r")
        score = fichier.readline()
        fichier.close()
        scoreJoueur, scorePC = score.split()
        return int(scoreJoueur), int(scorePC)
    except Exception:
        return 0, 0

def ecrireScore(scoreJoueur, scorePC):
    try:
        fichier = open("score/score.txt", "w")
        fichier.write(f"{scoreJoueur} {scorePC}")
        fichier.close()
        return 0
    except Exception:
        return "Fichier introuvable"

def reinitialiserScore():
    ecrireScore(0, 0)