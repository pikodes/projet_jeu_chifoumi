def calcul_point(matches, joueur) :
    point = {j: 0 for j in joueur}
    for match in matches :
        if len(match) != 3 :
            print("match invalide ignoré : " , match)
            continue
        j1, j2, resultat = match
        if resultat == "p1" :
            point[j1] += 3
        elif resultat == "p2" :
            point[j2] += 3
        elif resultat == "nulle" :
            point[j1] += 1
            point[j2] += 1
    return point
#test
joueur =["a", "b", "c","d"] 
match = [
    ("a", "b", "p1"),
    ("c", "d", "nulle"),
    ("a", "c", "p2"),
    ("b", "d", "p2")
]        
print(calcul_point(match, joueur))
         
