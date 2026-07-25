def moyenne_avec_arret(nombre):
	somme = 0
	compt = 0
		
	if nombre != -1 :
		somme += nombre 
		compt += 1
	
	if compt > 0 :
		moyenne = somme / compt
		return (f"la moyene est {moyenne}")
	else:
		return (f"veuillez entrez des moyenne ")


while True:
	nombre = float(input("Entrez la amoyenne : "))
	if nombre == -1:
		break
	

print(moyenne_avec_arret(nombre))