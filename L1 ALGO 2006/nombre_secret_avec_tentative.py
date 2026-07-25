# RAKOTOSON  
# Rico
# DA2I L1 Groupe B
# Matricule : 238I26 
nombre_secret = 50
tentative = int(input("entrez votre nombre : ")) 
if tentative == 50 :
    print("correct")
else :
    print("incorrect")
nombtre_tentative = 0
import time #maka lera 

while tentative != nombre_secret :
    nombtre_tentative = (nombtre_tentative + 1)
	
    if nombre_tentative == 3 :
	time.sleep(5)


    tentative = int(input ("entrez un  nouveau nombre : "))
    if tentative < nombre_secret :
        print("trop petit")
    elif tentative > nombre_secret :
        print("trop grand")
    elif tentative == nombre_secret :
        print("correct")
        print("Bravo ! Trouvé en ", nombtre_tentative,"tentatives")

        break
    