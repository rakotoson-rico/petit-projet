nombre = float(input("Entrez votre nombre : "))
def nombre_premier(nombre):
	import math
	compt = 0 
	for i in range(2,int(math.sqrt(nombre)+1)) :
		if  nombre % i == 0 : 
			compt += 1
			return(f"le nombre {nombre} n'est pas un nombre premier .") 
		elif compt == 0 : 
			return(f"le nombre {nombre} est un nombre premier .")
			
print(nombre_premier(nombre))
