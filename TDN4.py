# def minimum(listes):
#     minimun = listes[0]
#     for i in listes :
#         if i < minimum: 
#             minimum = i  
#     print(minimun)

# my_liste = [12,14,19,3,8]
# liste = minimum(my_liste)
# print(liste)

# ===========methode 1=============
def Calcul_moyenne(liste):
    somme = 0
    coef = 0
    for i in liste:
        somme += i
        coef += 1
        moyenne = somme/coef
    return f" Moyenne = {moyenne:.2f}"

notes = [12,15,9,18,10]
x= Calcul_moyenne(notes)
print(x)

# ===========methode2==========

def  somme(listes):
    somme =0
    for liste  in listes:
        somme += liste 
    return somme 

def coef(listes):
    coef = 0
    for liste in listes:
        coef += 1
    return coef 

def moyenne(liste):
    return f"La moyenne est : {somme(liste)/coef(liste):.2f}"
print(moyenne(notes))



# ============trouver l element lez plus grand ============
def plusGrand(liste):
    max = liste[0] #INITIALISENA HO VOLOANY 
    for i in liste :
        if i > max : #comparena @igny d ajoutena @ aloa ny bvaleurny 
            max = i
    position = liste.index(max) #index() afahana mmantatr aposition misqy anazy 
    return f"Le maximum est {max}, à la position {position}"
valeurs = [8,2,17,4,9]
print(plusGrand(valeurs))



def maximum(liste):
    max = liste[0]
    for i in max :
        max = i
    return max 
# ==========position==========
def positions(liste):
    return liste.index(max)


# def appel()
# positions(valeurs)
# ========element sup a 10============
liste = [5,12,7,14,10,18]
def TrouveSup10(listes):
    compteur = 0
    for i in listes:
        if i > 10 :
            compteur +=1
    return f"Nombre de valeurs > 10 : {compteur}"
print(TrouveSup10(liste))


# ==========iverser une liste ============
listes = [1,2,3,4,5]
def Inverser(liste):
    iverse= []
    compt = 0
    for i in liste :
        compt -=1
        iverse.append(liste[compt])
    return(f"Liste iversée : {iverse}")
print(Inverser(listes))


# ========== trouver si une valeur est present =========== 
liste=[3,7,2,9,5]
def TrouverValeur(listes):
    valeur = 9
    trouver = 0
    for valeurs in listes:
        # comparene @nazy aby heky 
        if valeurs == valeur:
            trouver = 1
    if trouver==1:
        return f"Valeurs trouvée ? {True}"
    else: return f"Valeurs trouvée ? {False}"
print(TrouverValeur(liste))


# ===========extraire les element pairs =================
def ElementPair(liste):
    pairs = []
    for i in liste:
        if i%2 ==0 :
            pairs.append(i)
    return f"Nombres pairs : {pairs}"
listes = [4,7,12,5,6,3]
print(ElementPair(listes))


# =========vérifier si la liste est trié en orde croissant===========
def OrdreCroissant(liste):
    premier= liste[0]
    test = 0
    est_trie = 0
    for  i in liste:
        if i > premier:
            test +=1
            premier = liste[test]
            
    return est_trie

listes =[2,4,6,10,7,9]
print(OrdreCroissant(listes))




# ==========le preoduit de tous======= 
def produit(liste):
    produit=1
    for i in liste:
        produit = produit *i
    return f"Produit = {produit}"

listes = [2,3,4]
print(produit(listes))


# ==========supprimer doublon ==========
def SupDoule(liste):
    val1 = liste[0]
    compt =0
    sans_doublons =[]
    for list in liste :
        if list > val1:
            compt+=1
            val1=liste[compt]
            sans_doublons.append(list)
    return f"Liste sans doublons : {sans_doublons}"

liste = [1,2,3,2,4,1,5]
print(SupDoule(liste))