def demander_age():

#Definit dans le context de la focnctionj zay ny ilmna return

	age =0
	while age == 0:
		age_str = input("votre age : ")
		try :
			age = int(age)
		except:
			print("ERREUR")
	return age 


age = demander_age()
print(age)