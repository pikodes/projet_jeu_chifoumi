def podium(point):
   """"charger du classement des joueurs"""
   classement = sorted(point.items(), key=lambda x: x[1], reverse=True)
   print("podium")
   print("1er : ",  classement[0][0])
   print("2e : ", classement[1][0])
   print("3e :", classement[2][0])
   return point

#test
point = {
   "a":10,
   "b":7,
   "c":12,
   "d":2
}
print(podium(point))