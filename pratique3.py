def classement_joueur(point):
#   """charger du ranking des participants tout au long du parcours"""
   if point >=100 :
      return "premier"
   elif point < 100 and point >50 :
     return "deuxieme"
   elif point < 50 and point > 30 :
      return "troisieme"
   else:
      return "perdant"
   
#test
print(classement_joueur(100))
print(classement_joueur(60))  
print(classement_joueur(20))
   
