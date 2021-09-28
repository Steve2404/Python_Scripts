nombre1 = nombre2 = ""
while not (nombre1.isdigit() and nombre2.isdigit()):
    nombre1 = input("Entrez un premier nombre: ")
    nombre2 = input("Entrez un deuxieme nombre: ")
    if not (nombre1.isdigit() and nombre2.isdigit()):
        print("Veillez entrez des nombres valides !!!")
    

print(f"Le resultat de l' addition de {nombre1} avec {nombre2} est egal à: {int(nombre1)+int(nombre2)}")