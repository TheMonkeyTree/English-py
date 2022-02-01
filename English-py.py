#! /usr/bin/env python
# -*- coding: Utf-8 -*-
import os, random, sys

def somme(liste):
    _somme = 0
    for i in liste:
        _somme = _somme + i
    return _somme
    
fichier = open("C:\\Users\\Spin1_Jo\\Desktop\\Anglais de A à Z\\129 ever et never.txt",'r',encoding="utf-8")
                  
              
tab = fichier.readlines()
n=len(tab)
print(n)

poids = [0]*(n)


for i in range(n):
    choice = random.randrange(0,n)
    while (poids[choice]==1):
        choice = random.randrange(0,n)
    if (poids[choice]==0):
        
        print("ligne n° : ",choice+1,"\t Phrases réussies : ",somme(poids),"/",n)
        phrases = tab[choice].split('_')
        
        print('')
        print(phrases[1])
        sentence = input("trad? : ")
        if (len(sentence)==1 and sentence!='w'):
            sys.exit("Fin de partie")
        if (sentence=='w'):
            print("Je passe")
            sentence='je passe'
            continue
        while (sentence != str(phrases[0]) and sentence!='je passe') :
            print("perdu :\t\t",phrases[0])
            sentence = input("trad? :\t\t")
            if (sentence=='p'):
                print("Je passe")
                sentence='je passe'
                continue
        print("\n\t-----------------  OK  ---------------")
        poids[choice]=1
print("##### FIN DU FICHIER #####") 
fichier.close()


