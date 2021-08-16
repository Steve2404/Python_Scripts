import math

class Point(object):
    
    "Definition dune classe point"

    def __init__(self):
        abs = 0
        ord = 0

    def distance(self, x, y):
        self.abs = x
        self.ord = y
        dist = math.sqrt((self.abs**2) + (self.ord**2))
        return dist
    

   
p9 = Point()
p9.x = 9
p9.y = 5
print(p9.x) 
longueur = p9.distance(4, 5)
print(longueur)
print(p9.__dict__)