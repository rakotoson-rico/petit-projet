#RAKOTOSON
#Rico
#Matricule : 413I26
#DA2I L1 GROUPE B

n = int(input("Entrez le nombre de nombre que vous voullez entrer : "))
compt_positif = 0
for i in range(1,n) :
	nombre = float(input("Entrez un nombre : "))
	if nombre >= 0 :
		compt_positif += 1
print(f"il y a {compt_positif} nombre positif") 
	