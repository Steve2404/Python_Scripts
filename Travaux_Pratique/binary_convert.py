ma_liste = list()
nombre = int(input('Entrez un nombre: '))
divande = nombre//2
reste = nombre%2
ma_liste.append(reste)
while divande !=0:
	reste = divande%2
	divande = divande//2
	ma_liste.append(reste)

ma_liste.reverse()
if len(ma_liste ) <= 4:
	c = '0'+'0'+'0'+'0'
elif len(ma_liste) == 5 :
	c = '0'+'0'+'0'
elif len(ma_liste) == 6 :
	c = '0'+'0'
elif len(ma_liste) == 7:
	c = '0'
else:
	c = ''

	
for elt in ma_liste:
	c = c+ str(elt)

print(c)	