
def joueur_match(parametre_part,parametre_joueur):
       """verifie si le nbre de personne correspond et complète si insufissant"""
       machine=0

       if parametre_part==4:
           if parametre_part<parametre_joueur:   
              nombre_de_joueur_partie=parametre_part
              nombre_joueur_ordinateur= parametre_part-parametre_joueur
              return nombre_de_joueur_partie ,nombre_joueur_ordinateur

           if parametre_part==parametre_joueur:
               nombre_de_joueur_partie=parametre_part
               nombre_joueur_ordinateur= parametre_part-parametre_joueur
               return nombre_de_joueur_partie ,nombre_joueur_ordinateur
           elif parametre_part>parametre_joueur:
               print("les nombres de joueurs sont supérieur aux participants: Recommencer")

       if parametre_part==8:
           if parametre_part<parametre_joueur:   
              nombre_de_joueur_partie=parametre_part
              nombre_joueur_ordinateur= parametre_part-parametre_joueur
              return nombre_de_joueur_partie ,nombre_joueur_ordinateur

           if parametre_part==parametre_joueur:
               nombre_de_joueur_partie=parametre_part
               nombre_joueur_ordinateur= parametre_part-parametre_joueur
               return nombre_de_joueur_partie ,nombre_joueur_ordinateur
           elif parametre_part>parametre_joueur:
               print("les nombres de joueurs sont supérieur aux participants: Recommencer")
       if parametre_part==16:
           if parametre_part==16 and parametre_joueur>=8:
             if parametre_part<parametre_joueur:   
                nombre_de_joueur_partie=parametre_part
                nombre_joueur_ordinateur= parametre_part-parametre_joueur
                return nombre_de_joueur_partie ,nombre_joueur_ordinateur

             if parametre_part==parametre_joueur:
                nombre_de_joueur_partie=parametre_part
                nombre_joueur_ordinateur= parametre_part-parametre_joueur
                return nombre_de_joueur_partie ,nombre_joueur_ordinateur
             elif parametre_part>parametre_joueur:
                  nombre_de_joueur_partie=parametre_part
                  nombre_joueur_ordinateur= parametre_part-parametre_joueur
                  return nombre_de_joueur_partie ,nombre_joueur_ordinateur
           else:
               print("pour une partie de jeu de 16 joueurs, le nombres minimun de participant doit être de 8 ")