##question 1
# application de l'algorithme de tri a bulle
def sort_list(liste_a_trie:list)->list:
    liste_copy=liste_a_trie.copy()
    for element in liste_a_trie:
        for i in range(len(liste_a_trie)-1):
            if liste_copy[i]>liste_copy[i+1]:
                liste_copy[i],liste_copy[i+1]=liste_copy[i+1],liste_copy[i]
    return liste_copy

##question 2

import time
import random

def mesure(func:callable,iter:int,taille:list,config:int)->float:
    liste_temps=[]
    for i in range(len(taille)):
        if config==1:
            liste=[random.randint for random.randint in range(taille[i])]
        elif config==2:
            liste=[item for item in range(taille[i])]
        elif config==3:
            liste=[item for item in range(taille[i],-1,-1)]
        temps=0
        for j in range(iter):#genere une liste de taille taille[i] pour les
            debut=time.perf_counter()#demarre le chrono
            func(liste)#execute la fonction
            fin=time.perf_counter()#arrete le chrono 
            temps_total=fin-debut
            temps+=(temps_total)
        liste_temps.append(temps/iter)#"{:.2e}".format() pour l'ecriture
    return liste_temps #scientifique mais c'est en str