# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 18:38:09 2020

@author: steve
"""


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
        
     
