def saisie():
        #saisie nombre de participant et personne dans le jeu avec gestion d'erreur 
        """
        try:  
           x,y=0,0
           while x!=4 or x!=8 or x!= 16:  
               y = int(input("entrez nombre de joueur : "))
               x = int(input("entrez nombre de participants [choix possible (4:8:16) nb:16 si nbre de joueur >=8] : "))
           if y<8 and x==16:
                print("pour un nombre total de participant égal à 16, le nombre de jouer doit être de 8 minimun")
                while x!=4 or x!=8 or x!= 16: 
                     y = int(input("entrez nombre de joueur : "))
                     x = int(input("entrez nombre de participants [choix possible (4:8:16) nb:16 si nbre de joueur >=8] : "))

        except ValueError:
          print('entrez nombre valide')
          y = int(input("entrez nombre de joueur : "))
          x = int(input("entrez nombre de participant [choix possible (4:8:16) nb:16 si nbre de joueur >=8] : "))
          return x,y
        except TypeError:
          print('entrez bonne combinaison')
          y = int(input("entrez nombre de joueur : "))
          x = int(input("entrez nombre de participant [choix possible (4:8:16) nb:16 si nbre de joueur >=8] : "))
          return x,y
        else:
            return x,y
        finally:
            print('bonne partie!')
            """
  

  
        while True:
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


