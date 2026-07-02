
def compter_voyelle(listes):
    voyelle = "aeyuio"
    nb_voyelle = 0
    for list in listes:
        if list in voyelle:
            nb_voyelle += 1
    return f"Nombre de voyelle : {nb_voyelle}"

texte = "programmation"
print(compter_voyelle(texte))

def palindrome(mots):
    inverserse_mot = []
    for mot in mots:
        inverserse_mot.insert(0,mot)
    if inverserse_mot == mots:
        return True
    else: return False
    
mot = "radar"
list_mot = list(mot)
print(palindrome(list_mot))

# deuxième grand rlement 
liste = [10,5,8,20,15]
premier = []
deuxieme = []
val = liste[0]
for list in liste:
    if list> val :
        premier.append(list)
print(premier)


# # fusionner 
# def fussioner(x,y):
#     fusion = []
#     for i in x and y :
#         if x != y :
#             fusion.append(x)
#     return fusion
# a = [1,2,3]
# b =[3,4,5]
# print(fussioner(a,b))  



# ======= remplacer_negatif ======= 
def remplacer_negatif(listes):
    nouveau_liste = []
    for list in listes:
        if list < 0:
            nouveau_liste.append(list* -1)
        else:
            nouveau_liste.append(list)
    return f"Liste modifiée : {nouveau_liste}"

liste = [4,-3,5,-2,0]
print(remplacer_negatif(liste))



def afficher_index_egaux(listes):
    valeur = 7
    indices = []
    for list in listes:
        if list == valeur:
            indices.append(list)
    return f"Indices de {valeur} : {indices}"

liste = [4,7,3,7,2,7]
print(afficher_index_egaux(liste))


