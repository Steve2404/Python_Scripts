import math
import random

var1, var2 = 0, 0
ligne, colonne = 4, 4
lst = [["0"]*colonne for _ in range(ligne)]

while var1<4 and var2<4:
    print(var1 , var2)
    var1= random.randrange(3)
    var2= random.randrange(3)
    lst[var1][var2]= "*"
    for i in range(var1):
        print(lst[i][var2])