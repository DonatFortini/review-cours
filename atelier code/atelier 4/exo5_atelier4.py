import random
import time
import matplotlib.pyplot as plt
import numpy as np

def mix_list(list_to_mix:list)->list:
    retour=list_to_mix.copy()#je copie la liste
    utilisé=[item for item in range(len(list_to_mix))]
    #  je stock les nombre de 0 a len
    for i in range(len(list_to_mix)):
        rand=random.choice(utilisé)
        retour[i]=list_to_mix[rand]#je prend un element aleatoire de la liste 
        utilisé.remove(rand)#et l'affecte a retour[i] 
        #et je le remove pour eviter les repetitions
    return retour

def mesure(func:callable,iter:int,taille:list)->float:
    liste_temps=[]
    for i in range(len(taille)):
        temps=0
        for j in range(iter):
            list_rando=[i for i in range(taille[i])]
            debut=time.perf_counter()
            func(list_rando)
            fin=time.perf_counter()
            temps_total=fin-debut
            temps+=(temps_total)
        liste_temps.append("{:.2e}".format(temps/iter))
    return liste_temps

def perf_mix(func1:callable,func2:callable,taille_liste:list,nb_iteration:int)->tuple:
    result1=mesure(func1,nb_iteration,taille_liste)
    result2=mesure(func2,nb_iteration,taille_liste)
    result_final=((result1),(result2))
    return result_final

res1,res2=(perf_mix(mix_list,random.shuffle,[10,100,1000,10000],10))

##question 1

def trace_cour(resultat1:list,resultat2:list):
    resultat1=np.arange(resultat1)
    resultat2=np.arange(resultat2)
    fig, ax = plt.subplots()
    
    ax.plot(resultat1,resultat1**2, 'r*-', label='fonction 1')
    ax.plot(resultat2,resultat2**3,'g*-', label='function 2')
    ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',
    title='Fonctions identité, cube et carré')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    
    plt.show()


trace_cour(res1,res2)