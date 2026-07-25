# RAKOTOSON 
# Rico 
# DA2I L1 Group B 
#Matricule : 238I26
m = int(input("Entrez une année : "))
a = m % 19
b = m % 4
c = m % 7

Tp =int(input(" 0 pour Grégorien et 1 pour Julien : "))

if Tp == 0 :
    G = 24
    N = 5
elif Tp == 1 :
    G = 15
    N = 6   
d = (19 * a + G) % 30

e =(2*b + 4*c + 6*d + N) % 7

p = d + e 
# date + 22 mars 
if p < 10 :
    x = p + 22 
    mois = "mars"
elif p > 9 :
    x = p - 9
    mois = "avril"
print("En",m,",Pâques est le Dimanche",x,mois)