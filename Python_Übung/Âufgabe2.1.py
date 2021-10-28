import numpy as np
import math

# a. Erzeugen Sie einen Vektor
n = ""
liste = []
## prüfen die Variable n ob es ein Zahl ist
while  not n.isdigit():
    n = (input("Geben Sie die Größe des Vektors: "))
n = int(n)

for i in range(0, n):
    zahl = i * 1 / n
    liste.append(zahl)
vek = np.array(liste)
print(vek)

# b. Berechnen Sie den Vektor
new_liste = []
for el in liste:
   new_val = math.sin(math.pi*el)
   new_liste.append(new_val)
new_vek = np.array(new_liste)
print(new_vek)

#c. Erstellen ein Nx3 Matrix:
liste_mat = []
for i in range(n):
    liste1 = [1]
    liste1.append(liste[i])
    liste1.append(liste[i]**2)
    liste_mat.append(liste1)
mat_N_3 = np.array(liste_mat)
print(mat_N_3)
