mots_de_passe_df = "123ricost"
tentative = 0
while TRUE :
	mots_de_passe = str(input (f"Entrez votre mots de passe : "))
	if mots_de_passe != mots_de_passe_df :
		print(f"incorrect")
		break

	