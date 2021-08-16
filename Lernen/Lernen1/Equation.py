# Equattion du second degre de forme ax^2 +bx + c= 0
import math

# definition des parametres
a= float(input("Entrez la valeur de a"))
b= float(input("Entrez la valeur de b"))
c= float(input("Entrez la valeur de c"))

#Calul du discriminant
d= b*b - (4*a*c)
X1= (-b - math.sqrt(d))/(2*a)
X2= (-b + math.sqrt(d))/(2*a)
X= -b/(2*a)
if(d<0):
    print("Pas de solution possible")
elif(d>0):
    print("Deux solutions X1= %s et X2= %s" %(X1, X2))
elif(d==0):
    print("Une solution double X= %s" %(X))
else:
    print("Impossible de calculer ca dans C")