def somme_pair(nombre):
	somme = 0
	if nombre % 2 == 0 : 
		somme = somme + nombre
	return somme

nombren = int(input("nombre de nombre : "))
for i in range(nombren):
	nombre = int(input(f"votre valeur : "))
print(somme_pair(nombre))
 