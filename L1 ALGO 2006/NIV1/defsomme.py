def addition(a,b):
	return a + b


def soustraction(a,b):
	return a - b

def division(a,b):
	return a/b

def multiplication(a,b):
	return a*b

n1 = int(input("a = "))
n2 = int(input("b = "))

choix =int(input("- 0 pour addition\n-1 pour soustraction\n-2 pour division\n-3nmultiplication \n : "))

c = addition(n1,n2)
d = soustraction(n1,n2)
e = division(n1,n2)
if choix == 0 :
	print(c)
elif choix == 1 :
	print(d)
elif choix == 2 : 
	print()