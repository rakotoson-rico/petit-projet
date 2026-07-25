#RAKOTOSON 
#Rico
#Matricule 413I26
#DA2I L1 GROUPE B

nombre = float(input(f"Entrez un nombre : "))
max = nombre 
for i in range(10):
	nombre = float(input(f"Entrez un autre nombre : "))
	if nombre > max :
		max = nombre 
print(f"Le nombre maximum est {max:3.2f}")
