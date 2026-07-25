 
nombre_secret = 50
Tentative =int(input("Deviner le nombre : "))

compt = 0

import time 

while not Tentative == nombre_secret :
	Tentative =int(input("veuillez ressayer encore : "))	
	if Tentative < 50 :
		print(f"le nombre {Tentative} est trop petit")
		compt += 1
	if 40 <Tentative <60 :
		print("ALEFA FA KELY SISA ")
	elif Tentative > 50 :
		print(f"le nombre {Tentative} est trop grande")
		compt +=1
	if compt == 5 :
		time.sleep(3)
		print("Trop de tentetive ,vous avez perdu ")
		break
if Tentative == nombre_secret :
	print(f"Bravo , le nombre {Tentative} est la bonne ")