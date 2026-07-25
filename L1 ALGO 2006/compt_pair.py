compte = 0

for i in range(1,11):
    nbr = float(input("Votre nombre{0} : ".format(i)))

    if nbr % 2 == 0 :
        compte = compte + 1 
        
print("il y a {0} nombres paires ".format(compte))
        