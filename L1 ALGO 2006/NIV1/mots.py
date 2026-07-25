#RAKOTOSON
#Rico
#matricule 413I26
#DA2I LI Groupe B

import time 
mots_de_passe_df = '123ghost'
tentative = 0
mots_de_passe = input("Entrez votre mots de passe : ")

while not mots_de_passe = mots_de_passe_df :
	mots_de_passe = input("mots de passe incorecte veuillez resayer : ")
	tentative += 1
	if tentative == 3:
		time.sleep(5)
		tentative = 0
		
		
print("mots de passe correct ")