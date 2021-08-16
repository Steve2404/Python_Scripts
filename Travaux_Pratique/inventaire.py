# # programme qui trie une liste  element
# inventaire = [("pommes", 22),
#                   ("melons", 4),
#                   ("poires", 18),
#                   ("fraises", 76),
#                   ("prunes", 51),
#                   ]
# #Ici on inverse les elemnt de notre liste d inventaire
# inventaire_inverse = [(qtt, nom_fruit) for nom_fruit, qtt in inventaire]
#
# #On peut maintenant passer a la phase de trie
# inventaire = [(nom_fruit, qtt) for qtt, nom_fruit in sorted(inventaire_inverse, reverse=True)]
# print(inventaire_inverse)
# print(inventaire)
# -------------------------------------------Exemple2------------------------------------------------------


# --------------------------------------------Exemple3-----------------------------------------------------------
# Dictionnaire en parametre nomme d une fonction
parametre = {"sep": ">>", "end": "-\n"}
print("voici", "un", "exemple", "d appel", **parametre)