def saisie(x, y):
        #saisie nombre de participant et personne dans le jeu avec gestion d'erreur 
        try:    
           x = int(input("entrez nombre de participant : "))
           y = int(input("entrez nombre de joueur : "))
        except ValueError:
          print('entrez nombre valide')
        except TypeError:
          print('entrez bonne combinaison')
        finally:
            print('operation termine')
        
