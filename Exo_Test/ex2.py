ch= "chaine"
Nbr_char= len(ch)
i=0
drap= 0;

while i< Nbr_char:
    if(ch[i] == 'e'):
        drap= 1;
    i += 1

# Affichage
print("Le caractere \"e\" ",end =' ')
if drap == 1:
    print("est present", end =' ')
else:
    print("est introuvable", end =' ')
print(" dans la chaine", ch)
        
     


    
        
