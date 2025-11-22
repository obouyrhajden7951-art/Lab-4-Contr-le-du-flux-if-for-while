seuil = 10
notes = []
max_notes = 10  


compteur = 0
while compteur < max_notes:
    entree = input("Entrez une note ou 'stop' : ").strip()
    if entree.lower() == "stop":
        break
    try:
        note = float(entree)
        notes.append(note)
        compteur += 1
    except ValueError:
        print("Valeur incorrecte, merci d'entrer un nombre.")
        continue  
    print("Nombre maximal de notes atteint.")


for index, note in enumerate(notes, start=1):
    statut = "Admis" if note >= seuil else "Refusé"
    print(f"Étudiant {index} : note {note} → {statut}")


if notes:
    moyenne = sum(notes) / len(notes)
    print(f"Moyenne de la classe : {moyenne:.2f}")
    if moyenne >= 16:
        print("Mention : Très Bien")
    elif moyenne >= 14:
        print("Mention : Bien")
    elif moyenne >= 12:
        print("Mention : Assez Bien")
    elif moyenne >= seuil:
        print("Mention : Passable")
    else:
        print("Mention : Insuffisant")
