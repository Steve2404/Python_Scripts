# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:53:53 2020

@author: steve
"""


#Programme qui dit si une anne est bissextile 

bissextil = False
anne = input("Entrez une annee")
anne = int(anne)

if(anne % 400 == 0):
    bissextil = True
elif(anne % 100 == 0):
    bissextil = True
elif(anne % 4 == 0):
    bissextil = True
else:
    bissextil = False
    
    
if bissextil:
    print("L'annee est bissextile")
else:
    print("L'annee n'est pas bisssextile")