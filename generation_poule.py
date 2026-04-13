def generation_poule(nbre_joueur,ordinateur=0):
     """creation de phase de poule"""
     compteur=0
     """creation d'une poule de 4 joueurs"""
     if nbre_joueur==4 and ordinateur==0:
        joueurs1={input("entrez le nom du joueur: "): n-n for n in range(1, nbre_joueur+1)}
        #print(joueurs1)   
     elif nbre_joueur==4 and ordinateur!=0:
         joueurs1={input("entrez le nom du joueur: "): n-n for n in range(1, nbre_joueur-ordinateur+1)}
         for i in range (1, ordinateur+1):
              joueurs1[f"machine1-{i}"]=0
         
     """creation des poules avec 8 joueurs"""
     if nbre_joueur==8 and ordinateur==0:
            joueurs1={input("entrez le nom du joueur: "): n-n for n in range(1, 5)}
            joueurs2={input("entrez le nom du joueur: "): n-n for n in range(1, 5)}
            
     elif nbre_joueur==8 and ordinateur!=0:
         joueurs1={input("entrez le nom du joueur: "): n-n for n in range(1, nbre_joueur-ordinateur+1 ) if n<5 }
         if nbre_joueur-ordinateur<4 and nbre_joueur-ordinateur!=4:
           for i in range (1, (4-(nbre_joueur-ordinateur))+1):
              joueurs1[f"machine1-{i}"]=0
           for i in range (1, 5):
              joueurs2={f"machine2-{n}": n-n for n in range(1, 5)}
           #print(joueurs1,joueurs2)  

         elif 8>nbre_joueur-ordinateur>4 and nbre_joueur-ordinateur!=4:
            joueurs2={input("entrez le nom du joueur: "): n-n for n in range(1, nbre_joueur-ordinateur-4+1) if n<5}
            for i in range (1, ordinateur+1):
              joueurs2[f"machine2-{i}"]=0
            #print(joueurs1,joueurs2)
         elif nbre_joueur-ordinateur==4:
             joueurs2={f"machine2-{n}": n-n for n in range(1, 5)}
             #print(joueurs1,joueurs2)

     """creation des poules avec 16 joueurs    """     

     if nbre_joueur==16 and ordinateur==0:
            joueurs1={input("entrez le nom du joueur: "): n-n for n in range(1, 5)}
            joueurs2={input("entrez le nom du joueur: "): n-n for n in range(1, 5)}
            joueurs3={input("entrez le nom du joueur: "): n-n for n in range(1, 5)}
            joueurs4={input("entrez le nom du joueur: "): n-n for n in range(1, 5)}
            
     if nbre_joueur==16 and ordinateur!=0:
           
          joueurs1={}
          joueurs2={}
          joueurs3={}
          joueurs4={}
          dic_mere = {input("entrez le nom du joueur: "): n-n for n in range(1, nbre_joueur-ordinateur+1)} 

          
          #for nom,score in dic_mere.items()  i in range (1, len(dic_mere)+1):
          s1,s2,s3,s4=0,0,0,0
          for i, (nom, score) in enumerate(dic_mere.items(), start=1):
               if (len(joueurs1)==0 or (i-s1==4)) and (len(joueurs1)<=3):
                 joueurs1[nom]=score
                 s1=i
                 continue
               if (len(joueurs2)==0 or  i-s2==4) and len(joueurs2)<=3:
                 joueurs2[nom]=score
                 s2=i
                 continue
               if (len(joueurs3)==0 or  i-s3==4) and len(joueurs3)<=3:
                 joueurs3[nom]=score
                 s3=i
                 continue
               if (len(joueurs4)==0 or i-s4==4) and len(joueurs4)<=3:
                 joueurs4[nom]=score
                 s4=i
                 continue
               compteur+=1
          for i in range (1, 4-len(joueurs1)+1):
              joueurs1[f"machine1-{i}"]=0  
          for i in range (1, 4-len(joueurs2)+1):
              joueurs2[f"machine2-{i}"]=0
          for i in range (1, 4-len(joueurs3)+1):
              joueurs3[f"machine3-{i}"]=0
          for i in range (1, 4-len(joueurs4)+1):  
              joueurs4[f"machine4-{i}"]=0  
     #print(joueurs1,joueurs2,joueurs3,joueurs4, end=" ")
    



     
     
     if nbre_joueur==4:
            tous_joueurs4=[]
            for parametre1, parametre2 in joueurs1.items():
                 joueurx={}
                 joueurx["nom"]=parametre1
                 joueurx["points_recu"]=parametre2
                 joueurx["classement"]=0
                 joueurx["poule_joueur"]="poule 1"
                 tous_joueurs4.append(joueurx)
                  
            import csv
            with open("phase_poule.csv","w", newline="", encoding="utf-8") as fichier:
                colonnes=["nom","points_recu","classement","poule_joueur"]
                joueur_entres=csv.DictWriter(fichier,fieldnames=colonnes)
                joueur_entres.writeheader()
                joueur_entres.writerows(tous_joueurs4)
            return "phase_poule.csv"                
    
     elif nbre_joueur==8:
            tous_joueurs18=[] 
            for parametre1, parametre2 in joueurs1.items():
                 joueurx={}
                 joueurx["nom"]=parametre1
                 joueurx["points_recu"]=parametre2
                 joueurx["classement"]=0
                 joueurx["poule_joueur"]="poule 1"
                 tous_joueurs18.append(joueurx)

            import csv
            with open("phase_poule1.csv","w", newline="", encoding="utf-8") as fichier:
                colonnes=["nom","points_recu","classement","poule_joueur"]
                joueur_entres=csv.DictWriter(fichier,fieldnames=colonnes)
                joueur_entres.writeheader()
                joueur_entres.writerows(tous_joueurs18)                   
                
            tous_joueurs28=[]
            for parametre1, parametre2 in joueurs2.items():
                 joueurx={}
                 joueurx["nom"]=parametre1
                 joueurx["points_recu"]=parametre2
                 joueurx["classement"]=0
                 joueurx["poule_joueur"]="poule 2"
                 tous_joueurs28.append(joueurx)

            import csv
            with open("phase_poule2.csv","w", newline="", encoding="utf-8") as fichier:
                colonnes=["nom","points_recu","classement","poule_joueur"]
                joueur_entres=csv.DictWriter(fichier,fieldnames=colonnes)
                joueur_entres.writeheader()
                joueur_entres.writerows(tous_joueurs28)   

            return "phase_poule1.csv","phase_poule2.csv"                    

     elif nbre_joueur==16:
           tous_joueurs116=[]
           for parametre1, parametre2 in joueurs1.items():
                 joueurx={}
                 joueurx["nom"]=parametre1
                 joueurx["points_recu"]=parametre2
                 joueurx["classement"]=0
                 joueurx["poule_joueur"]="poule 1"
                 tous_joueurs116.append(joueurx)

           import csv
           with open("phase_poule1.csv","w", newline="", encoding="utf-8") as fichier:
                colonnes=["nom","points_recu","classement","poule_joueur"]
                joueur_entres=csv.DictWriter(fichier,fieldnames=colonnes)
                joueur_entres.writeheader()
                joueur_entres.writerows(tous_joueurs116)                   

           tous_joueurs216=[]
           for parametre1, parametre2 in joueurs2.items():
                 joueurx={}
                 joueurx["nom"]=parametre1
                 joueurx["points_recu"]=parametre2
                 joueurx["classement"]=0
                 joueurx["poule_joueur"]="poule 2"
                 tous_joueurs216.append(joueurx)

           import csv
           with open("phase_poule2.csv","w", newline="", encoding="utf-8") as fichier:
                colonnes=["nom","points_recu","classement","poule_joueur"]
                joueur_entres=csv.DictWriter(fichier,fieldnames=colonnes)
                joueur_entres.writeheader()
                joueur_entres.writerows(tous_joueurs216)                   

           tous_joueurs316=[]      
           for parametre1, parametre2 in joueurs3.items():
                 joueurx={}
                 joueurx["nom"]=parametre1
                 joueurx["points_recu"]=parametre2
                 joueurx["classement"]=0
                 joueurx["poule_joueur"]="poule 3"
                 tous_joueurs316.append(joueurx)

           import csv
           with open("phase_poule3.csv","w", newline="", encoding="utf-8") as fichier:
                colonnes=["nom","points_recu","classement","poule_joueur"]
                joueur_entres=csv.DictWriter(fichier,fieldnames=colonnes)
                joueur_entres.writeheader()
                joueur_entres.writerows(tous_joueurs316)                   

           tous_joueurs416=[]      
           for parametre1, parametre2 in joueurs4.items():
                 joueurx={}
                 joueurx["nom"]=parametre1
                 joueurx["points_recu"]=parametre2
                 joueurx["classement"]=0
                 joueurx["poule_joueur"]="poule 4"
                 tous_joueurs416.append(joueurx) 

           import csv
           with open("phase_poule4.csv","w", newline="", encoding="utf-8") as fichier:
                colonnes=["nom","points_recu","classement","poule_joueur"]
                joueur_entres=csv.DictWriter(fichier,fieldnames=colonnes)
                joueur_entres.writeheader()
                joueur_entres.writerows(tous_joueurs416)  

           return "phase_poule1.csv","phase_poule2.csv","phase_poule3.csv","phase_poule4.csv" 




