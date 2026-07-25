# RAKOTOSON 
# Rico 
# DA2I L1 Groupe B 
# Matricule 413I26
compt = 0
somme = 0
for i in range(10):
    nombre = int(input("Ecrire nombre n= "))
    if nombre % 2 == 0 :
        compt = compt + 1
        somme = somme + nombre


print("vous avez",compt,"nombres paires")
print("la somme de votre nombre est de: ",somme)
