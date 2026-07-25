#RAKOTOSON Rico 
#DA2I L1 Groupe B 
#Matricule : 413I26
nombre_de_nombre = int(input(f"Entrez le nombre de note que vous voullez : " ))
somme = 0
for i in range(nombre_de_nombre):
	valeur_du_nombre = float(input(f"Entrez la valeur du nombre : "))
	somme = somme + valeur_du_nombre 
	moyenne = somme / nombre_de_nombre
print(f"la moyenne est de {moyenne}")