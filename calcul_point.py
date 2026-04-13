

def calcul_point_poule(jeu_joueur1, jeu_joueur2):
  """ 
   calcul des points phases de poules
  Arg:
       nombre_essais (int) : nombre de tentatives
       niveau_jeux (str): "etape1", "etape2" ou "etape3"
  return:
       int: point calculé (0-50)
  """
  if jeu_joueur1==1 and jeu_joueur2==3:
        score_joueur1,score_joueur2=3,0

  elif jeu_joueur1==3 and jeu_joueur2==1:  
        score_joueur2,score_joueur1=3,0  

  elif jeu_joueur1==1 and jeu_joueur2==2:
        score_joueur2,score_joueur1=3,0

  elif jeu_joueur1==2 and jeu_joueur2==1:  
        score_joueur1,score_joueur2=3,0   

  elif jeu_joueur1==3 and jeu_joueur2==2:
        score_joueur1,score_joueur2=3,0

  elif jeu_joueur1==2 and jeu_joueur2==3:  
        score_joueur1,score_joueur2=3,0  

  elif jeu_joueur1==1 and jeu_joueur2==1 or jeu_joueur1==2 and jeu_joueur2==2 or jeu_joueur1==3 and jeu_joueur2==3:   
        score_joueur1,score_joueur2=1,1      

  return score_joueur1,score_joueur2

def calcul_point_elim(jeu_joueur1, jeu_joueur2):
  """ 
   calcul des points phases de poules
  Arg:
       nombre_essais (int) : nombre de tentatives
       niveau_jeux (str): "etape1", "etape2" ou "etape3"
  return:
       int: point calculé (0-50)
  """
  if jeu_joueur1==1 and jeu_joueur2==3:
        score_joueur1,score_joueur2=3,0

  elif jeu_joueur1==3 and jeu_joueur2==1:  
        score_joueur2,score_joueur1=3,0  

  elif jeu_joueur1==1 and jeu_joueur2==2:
        score_joueur2,score_joueur1=3,0

  elif jeu_joueur1==2 and jeu_joueur2==1:  
        score_joueur1,score_joueur2=3,0   

  elif jeu_joueur1==3 and jeu_joueur2==2:
        score_joueur1,score_joueur2=3,0

  elif jeu_joueur1==2 and jeu_joueur2==3:  
        score_joueur1,score_joueur2=3,0  

  elif jeu_joueur1==1 and jeu_joueur2==1 or jeu_joueur1==2 and jeu_joueur2==2 or jeu_joueur1==3 and jeu_joueur2==3:   
        score_joueur1,score_joueur2=1,1      

  return score_joueur1,score_joueur2
