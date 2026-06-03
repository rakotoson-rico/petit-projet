
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
print("votire epuation")

print(a,"x**2 +",b,"x +",c,"= 0")
D =(b*b + 4*(a*c))
print ("Delta = ",D)

import math # hitondrana ny racine 

if D<0 :
    print("solution vide")
elif D == 0 :
    x1 = x2 = -b/(2*a)
    print("x1 = x2 =",x1)
elif D > 0 :
    print("{0} = {1}".format("x1",((-b + math.sqrt(D))/2*a)))
    print("{0} = {1}".format("x2",((-b - math.sqrt(D))/2*a)))