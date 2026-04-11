MAX_ESSAIS = 3
FICHIER_POINTS = "point.txt"

def calcul_point(nombre_essais, niveau_jeux):
  """ 
   calcul des points phases de poules
  Arg:
       nombre_essais (int) : nombre de tentatives
       niveau_jeux (str): "etape1", "etape2" ou "etape3"
  return:
       int: point calculé (0-50)
  """
  score_base = 0
  penalite = nombre_essais * 10
  if niveau_jeux == "etape3" :
    score_base = 9
  elif niveau_jeux == "etape2" :
    score_base = 6
  else:
    score_base = 3

  score_final = max(0, penalite - score_base)
  return score_final 
#test
essais = 2
score = calcul_point(essais,"etape3" )

print(f"Point final : {score} point")


   
