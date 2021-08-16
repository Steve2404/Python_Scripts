import  os
import pickle



os.chdir("C:/Users/Steve/Documents/Python Scripts/Lernen/Lernen2")
#-----------------------------------Lecture_Fichier----------------------------------------------
# liste = list()
# mon_fichier = open("fichier.txt", "r")
# contenu = mon_fichier.read()
# liste = contenu.split()
# print(contenu)
# print(liste)
# mon_fichier.close()

#--------------------------------------Ecriture_Fichier----------------------------------------------
# mon_fichier = open("fichier.txt", "w")
# mon_fichier.write("Premier test d ecriture dans un fichier via python")
# mon_fichier.close()

#------------------------------------Autre_facon_avec_with----------------------------------------
# with open("fichier.txt", "r") as mon_fichier:
#     contenu = mon_fichier.read()
#     print(contenu)
# print(mon_fichier.closed) # Verifie la fermeture ou l ouverture du fichier

#_______________________________Class_pickle__________________________________
#-------------------------------------Ecriture_Fichier_Pickler---------------------------------------
# score = {
#     "joueur1" : 10,
#     "joueur2": 24,
#     "joueur3": 29,
#     "joueur4": 24,
# }
# with open("donne", "wb") as fichier:
#     mon_pickler = pickle.Pickler(fichier)
#     mon_pickler.dump(score)  # Ajoute un element dans le pickle

#--------------------------------------Lecture_Fichier_Unpickler-----------------------------------
with open("donne", "rb") as fichier:
    mon_pickle = pickle.Unpickler(fichier)
    score_recupere = mon_pickle.load() # Recuperation dun Element dans notre pickle
    print(score_recupere)