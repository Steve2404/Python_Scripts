from turtle import*

def triangle(couleur):
    " Fontion qui dessine un triangle equilaterale"
    a= 0
    while a<3:
        color(couleur)
        forward(100)
        left(120)
        
        a= a+1
    

print(triangle.__doc__) 

triangle('red')
