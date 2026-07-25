valeur = int(input("nombre de nombre : "))

def compter_pair(valeur):
	
	compt = 0
	for i in range(0,int(valeur) + 1):
		
		if i % 2 == 0 :
			compt = compt + 1
	return compt #manapaky asa koa 

pair = compter_pair(valeur)

print(f" il y a {pair} nombre pair ")	

#return valin fonction 
 