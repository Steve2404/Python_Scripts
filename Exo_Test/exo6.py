# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 01:57:23 2020

@author: steve
"""

#Afficher le grand element d une liste

t= [32,15,12,8,3,75,2,15]
max= 0
i= 0

while i< len(t):
    if t[i]>max:
        max= t[i]
    i= i+1

print(" Le plus grand element de cette liste a la valeur ", max)
        