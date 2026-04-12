def le_jeux(jeux):
 # """s'occupe des affrontements entre joueurs en affichant le jeux de l'utilisateur"""
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
print(le_jeux(jeux))      
      


      

