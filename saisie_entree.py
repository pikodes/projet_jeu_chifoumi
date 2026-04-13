def saisie():

  

  
        
          try:
            x = int(input("entrez nombre de participant [choix possible (4:8:16) nb:16 si nbre de joueur >=8] : "))
            y = int(input("entrez nombre de joueurs :"))

            if x <= 0:
                    print("Erreur : le nombre de participants doit être positif")
            elif y <= 0:
                    print("Erreur : le nombre de joueurs par groupe doit être positif")
            elif x not in [4, 8, 16]:
                    print("Erreur : le tournoi accepte seulement 4, 8 ou 16 joueurs")
            elif y<8 and x==16:
                    print("Erreur : pour un nombre total de participant égal à 16, le nombre de jouer doit être de 8 minimun")
            else:
                   return x, y  

          except ValueError:
                  print("Erreur : tu dois entrer un nombre entier")


def saisie_jeu_poule():
        
        
        while True:

          try:
            choisir=(1,2,3)
            jeux_joueur = int(input("que vas tu jouer:entre juste le chiffre affecter à ton jeu [pierre=1, papier=2, ciseau=3]"))

            if jeux_joueur!=[1,2,3]:
                    print("Erreur : jeux non pris en charge bien lire les consignes")
                    jeux_joueur = int(input("que vas tu jouer:entre juste le chiffre affecter à ton jeu [pierre=1, papier=2, ciseau=3]"))

                    return jeux_joueur 

          except ValueError:
                  print("Erreur : tu dois entrer un nombre entier")

"""def saisie_jeu_elim():
         
         while True:
          try:
            jeux_joueur = int(input("que vas tu jouer:entre juste le chiffre affecter à ton jeu [pierre=1, papier=2, ciseau=3]"))
            

            while jeux_joueur!=[1,2,3] :
                    print("Erreur : jeux non pris en charge bien lire les consignes")
                    jeux_joueur= int(input("que vas tu jouer:entre juste le chiffre affecter à ton jeu [pierre=1, papier=2, ciseau=3]"))
    
            while jeu1==jeu2:
                    print("Erreur : jeux equivalent modifier")
                    jeu1 = int(input("que vas tu jouer:entre juste le chiffre affecter à ton jeu [pierre=1, papier=2, ciseau=3]"))
                    jeu2 = int(input("que vas tu jouer:entre juste le chiffre affecter à ton jeu [pierre=1, papier=2, ciseau=3]"))
            return jeux_joueur

          except ValueError:
                  print("Erreur : tu dois entrer un nombre entier")"""


