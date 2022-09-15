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


#la fonction calcule temps d'execution d'une func passé en parametre pour un 
#nombre d'iteration iter,et stock tout les resultat dans une liste
def mesure(func:callable,iter:int,taille:list)->float:
    liste_temps=[]
    for i in range(len(taille)):
        temps=0
        for j in range(iter):#genere une liste de taille taille[i] pour les
            list_rando=[i for i in range(taille[i])]# iter tests à venir
            debut=time.perf_counter()#demarre le chrono
            func(list_rando)#execute la fonction
            fin=time.perf_counter()#arrete le chrono 
            temps_total=fin-debut
            temps+=(temps_total)
        liste_temps.append(temps/iter)#"{:.2e}".format() pour l'ecriture
    return liste_temps #scientifique mais c'est en str

def perf_mix(func1:callable,func2:callable,taille_liste:list,nb_iteration:int)->tuple:
    result1=mesure(func1,nb_iteration,taille_liste)
    result2=mesure(func2,nb_iteration,taille_liste)
    result_final=((result1),(result2))
    return result_final

res1,res2=(perf_mix(mix_list,random.shuffle,[10,100,1000,10000],10))


##question 1

def trace_courbe(resultat1:list,resultat2:list):
    resultat1=np.arange(resultat1[0],resultat1[-1],0.05)
    resultat2=np.arange(resultat2[0],resultat2[-1],0.0005)
    fig, ax = plt.subplots()
    
    ax.plot(resultat1,resultat1**5, 'r*-', label='fonction 1')
    ax.plot(resultat2,resultat2,'g*-', label='function 2')
    ax.set(xlabel='temps execution en ms', ylabel='taille des listes',title='Comparaison de fonction')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    
    plt.show()


trace_courbe(res1,res2)