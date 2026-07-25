n = input("saisir mots de passe : ")
mot = 1040
import time 
for i in range(1,5):
	if n == mot :
		print(f"correct")
	else:
		print(f"incorrect")
		time.sleep(5)
print("correct i ")