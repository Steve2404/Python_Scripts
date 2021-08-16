print("la suite de Fibonachi :")

a, b, c = 1, 1, 1

while c < 11 :
    print(b, end=" ")
    a, b, c = b, b+a, c+1
