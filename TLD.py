# ======= tuplrs ==========
t1 = (1,2,3,4,5)
print(t1)
print(len(t1)) # afahana mamantatra ny longers 
b = t1[2:5]
print(b) #aseony ny postion 2 just 5-1
premier = t1[:4] #maneo ny debut just 4-1
e = t1[-3:] #trois dernier 

t2 = (6,7,8,9)
print(t1+t2)
# repication 
print(t2*2)
# tuple de tuple ou tuple a deux dimession 
tup = ((1,2,3,9),(4,5,6),(7,8,9,10))
print(tup[2][-1]) #fidinao hek ny aia n hidirana d bakeo ny aia ny avoka @ ilay hidirana 
print(len(tup))
print(len(tup[0]))

# liste ===========
liste = [1,2,3]
print(liste)
liste [0] = 4 #afahana maova valeurs 
print(liste)
liste1 = []
liste1.append(liste[-1] )
print(liste1)
liste.insert(1,19) #postion asina anzy heky vo nu valeur 
print(liste)
liste1.insert(0,liste[0])
print(liste1)

del liste[-1] #mamafa 
print(liste)
# mamadika 
liste1.reverse()
print(liste1)
# manoy anaz àvaleur maro 
liste1.extend([55,22])
print(liste1)

# covertion d' ecriture // hanorona n au carre 
source = [1,5,8,12,7]
resulatat = []
for v in source:
    resulatat.append(v**2)
print(resulatat)
#  ze paire koa 
resulatat1 = []
for i in resulatat:
    if i %2 == 0:
        resulatat1.append(i**2)
print(resulatat1)

liste2 = [19,9,6,45]
# hitady plasy 
trouve = 19 in liste2
print(trouve)
print(6 in liste2)
print(4 in liste2 )

# index fahan maman(tatra position )

id = liste2.index(9)
print(id)

# remove manala 
liste2.remove(45)
print(liste2)
liste3 = []
liste4 = [1,5,6]
liste3 = liste4.copy()
print(liste3)

# chjaine de caractère 
chaine  = "bonjour le monde"
print(chaine)
print(len(chaine))

# tsy afak ovana n cahine 
# chaine[0] = "B"
# print(chaine) 
# mabnao majuscule nb aza adino n maisy () 
maj = chaine.upper()
print(maj)
# place 
id = maj.find("JO")
print(id)
nb = maj.count("ON")
print(nb)
manova = maj.replace("O" ,"A")
print(manova)

