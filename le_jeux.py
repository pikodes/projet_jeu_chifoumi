def le_jeux_poule(*nombres):

   for nombre in nombres: 
       
      from calcul_point import calcul_point_poule,calcul_point_elim
      from saisie_entree import saisie,saisie_jeu_poule
      import csv 
      from itertools import combinations
      from random import choice
      import pandas   
      combat={}
      recup_joueur=[]
      choisi_val=(1,2,3)
# Etape 1 : lire toutes les donnees dans une liste 
      with open("{nombre}", "r", encoding="utf-8") as fichier: 
           lecteur = csv.DictReader(fichier) 
           colonnes = lecteur.fieldnames 
           next(fichier)       # saute ['nom', 'prenom', 'age'] 
           partie_jeux = list(lecteur)            # toutes les lignes en memoire 
           for ligne in lecteur:
               combat[ligne["nom"]]=ligne["points_recu"]
               recup_joueur.append(ligne["nom"])
           matchs = list(combinations(combat["nom"], 2))    #####
           #score_partie=list(combinations(combat["points_recu"])) 
           for i, (joueur01, joueur02) in enumerate(matchs, start=1):
                  print(f"Match {i} : {joueur01} vs {joueur02}")
                  if joueur01=="machine":
                      jeu1,jeu2=choice(choisi_val),saisie_jeu_poule()
                  elif joueur02=="machine": 
                      jeu2,jeu1=choice(choisi_val),saisie_jeu_poule()
                  elif joueur02=="machine" and joueur01=="machine":
                      jeu1,jeu2=choice(choisi_val),choice(choisi_val)
                  elif  joueur02!="machine" and joueur01!="machine" :  
                        jeu1,jeu2=saisie_jeu_poule(),saisie_jeu_poule()
                  combat[joueur01],combat[joueur02]=(calcul_point_poule(jeu1,jeu2))

# Etape 2 : modifier les donnees en Python 
           for joueur in partie_jeux: 
               if joueur['nom'] in combat.keys(): 
                joueur['points_recu'] = combat[joueur]           # modification 
 
# Etape 3 : re-ecrire le fichier avec les modifications 
      with open("poule", "w", newline="", encoding="utf-8") as fichier: 
            ecrivain = csv.DictWriter(fichier, fieldnames=colonnes) 
            ecrivain.writeheader()               # re-ecrire l'en-tete 
            ecrivain.writerows(partie_jeux)         # re-ecrire toutes les lignes


      with open("poule.csv", "w", newline="", encoding="utf-8") as fichier: 
            data=pandas.read_csv('{nombre}.csv', sep=';')
            a=data.sort_values(by=['points_recu'], ascending=False)
            ecrivain = csv.DictWriter(fichier, fieldnames=colonnes) 
            ecrivain.writeheader()               # re-ecrire l'en-tete 
            for i in range (2) :
                  ecrivain.writerows(a)         # re-ecrire toutes les lignes
      return "poule.csv"
            
                  

          
def le_jeux_elim(*nombres):

   for nombre in nombres: 
       
      from calcul_point import calcul_point_poule,calcul_point_elim
      from saisie_entree import saisie,saisie_jeu_poule,saisie_jeu_elim
      import csv 
      from itertools import combinations
      from random import choice
      import pandas # type: ignore

      combat={}
      recup_joueur=[]
      choisi_val=(1,2,3)
        # Etape 1 : lire toutes les donnees dans une liste 
      with open("{nombre}", "r", encoding="utf-8") as fichier: 
           lecteur = csv.DictReader(fichier) 
           colonnes = lecteur.fieldnames 
           next(fichier)       # saute ['nom', 'prenom', 'age'] 
           partie_jeux = list(lecteur)            # toutes les lignes en memoire 
           for ligne in lecteur:
               combat[ligne["nom"]]=ligne["points_recu"]
               recup_joueur.append(ligne["nom"])
           matchs = list(combinations(combat["nom"], 2))    #####
           #score_partie=list(combinations(combat["points_recu"])) 
           combatant={}
           for i, (joueur01, joueur02) in enumerate(matchs, start=1):
                  print(f"Match {i} : {joueur01} vs {joueur02}")
                  if joueur01=="machine":
                      jeu1,jeu2=choice(choisi_val),saisie_jeu_poule()
                  elif joueur02=="machine": 
                      jeu2,jeu1=choice(choisi_val),saisie_jeu_poule()
                  elif joueur02=="machine" and joueur01=="machine":
                      jeu1,jeu2=choice(choisi_val),choice(choisi_val)
                  elif  joueur02!="machine" and joueur01!="machine" :  
                        jeu1,jeu2=saisie_jeu_poule(),saisie_jeu_poule()
                  a,b=(calcul_point_elim(jeu1,jeu2))
                  if a>b:
                      combatant[joueur01]=0
                  else:
                      combatant[joueur02]=0   

           for ligne in (len(combatant)):
                matchs = list(combinations(combatant["nom"], 2))    #####
                #score_partie=list(combinations(combat["points_recu"])) 
                combatants={}
                for i, (joueur01, joueur02) in enumerate(matchs, start=1):
                     print(f"Match {i} : {joueur01} vs {joueur02}")
                     if joueur01=="machine":
                        jeu1,jeu2=choice(choisi_val),saisie_jeu_poule()
                     elif joueur02=="machine": 
                        jeu2,jeu1=choice(choisi_val),saisie_jeu_poule()
                     elif joueur02=="machine" and joueur01=="machine":
                        jeu1,jeu2=choice(choisi_val),choice(choisi_val)
                     elif  joueur02!="machine" and joueur01!="machine" :  
                         jeu1,jeu2=saisie_jeu_poule(),saisie_jeu_poule()   

                     if a>b:
                       combatant[joueur01]=0
                     else:
                      combatant[joueur02]=0   

      for nom in combatant: 
          print(nom)                       
                        
     


   



                    