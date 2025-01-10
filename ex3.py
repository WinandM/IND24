def calculer_somme(notes):
    addNote = 0
    addNoteMax = 0
    for key, values in notes.items():
        addNoteMax += int(key) * len(values)
        for value in values:
            addNote += int(value)
    print(f"Somme des notes {addNote} / {addNoteMax}")
    return addNote, addNoteMax

def calculer_moyenne(totalNote, totalMax, moyenne):
    return totalNote / totalMax * moyenne

def calculer_pourcentage(totalNote, totalMax):
    return calculer_moyenne(totalNote, totalMax, 100)

moyenne = int(input("Entrez la note sur laquelle la moyenne va être calculée: "))
continuer = True
notes = {"0": {}}
while continuer:
    noteMax = int(input("Entrez la note maximale: "))
    note = input("Entrez les notes (séparées par des espaces): ")
    if str(noteMax) in notes.keys():
        notes[str(noteMax)].append(note.split())
    else:
        notes[str(noteMax)] = note.split()
    if input("continuer o/n? ") == "n":
        continuer = False

totalNote, totalNoteMax = calculer_somme(notes)
print(f"Moyenne des notes {calculer_moyenne(totalNote, totalNoteMax, moyenne)} / {moyenne}")
print(f"Pourcentage des notes {calculer_pourcentage(totalNote, totalNoteMax)} / 100")