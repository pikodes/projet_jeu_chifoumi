def le_jeux():
  """s'occupe des affrontements entre joueurs en affichant le jeux de l'utilisateur
   if jeux == "a":
      return "pierre"
   elif jeux== "b":
      return "papier"
   elif jeux == "p":
      return "ciseaux"
   else:
      return None

#tests
jeux = input("Entrez jeux : ")      
print(le_jeux(jeux))      """
      


from calcul_point import calcul_point_poule,calcul_point_elim
from saisie_entree import saisie,saisie_jeu_poule,saisie_jeu_elim
        
import csv 
from itertools import combinations

combat={}
recup_joueur=[]
# Etape 1 : lire toutes les donnees dans une liste 
with open("{sortie_genera_poule}", "r", encoding="utf-8") as fichier: 
    lecteur = csv.DictReader(fichier) 
    colonnes = lecteur.fieldnames 
    next(fichier)       # saute ['nom', 'prenom', 'age'] 
    partie_jeux = list(lecteur)            # toutes les lignes en memoire 
    for ligne in lecteur:
        combat[ligne["nom"]]=ligne["points_recu"]
        recup_joueur.append(ligne["nom"])
    matchs = list(combinations(combat["nom"], 2))    #####
    score_partie=list(combinations(combat["points_recu"])) 
    for i, (joueur01, joueur02) in enumerate(matchs, start=1):
         print(f"Match {i} : {joueur01} vs {joueur02}") 
         combat[joueur01],combat[joueur02]=(calcul_point_poule(saisie_jeu_poule()))

# Etape 2 : modifier les donnees en Python 
for joueur in partie_jeux: 
    if joueur['nom'] in combat.keys(): 
        joueur['points_recu'] = combat[joueur]           # modification 
 
# Etape 3 : re-ecrire le fichier avec les modifications 
with open("{sortie_genera_poule}", "w", newline="", encoding="utf-8") as fichier: 
    ecrivain = csv.DictWriter(fichier, fieldnames=colonnes) 
    ecrivain.writeheader()               # re-ecrire l'en-tete 
    ecrivain.writerows(partie_jeux)         # re-ecrire toutes les lignes
