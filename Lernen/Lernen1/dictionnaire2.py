
invent= {'pomme':430, 'banane':312, 'oranges':274, 'poire':137 } # definition d un dictionnaire
print(invent)
del invent['pomme'] # supprimer une cle
invent['citron']= 100 # ajout d un element dans le dictionaire
print(invent)

if 'pomme' in invent: # on teste toujour la cle
    print("Nous avons des pommes")
else:
    print("Pas de pomme. Sorry!!!")

tuple_ext= invent.items() # extration d une sequence equivalente de tuple
print(tuple_ext)
