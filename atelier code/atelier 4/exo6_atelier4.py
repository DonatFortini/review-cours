##question 1

def sort_list(liste_a_trie:list)->list:
    """la fonction tri des elements dans l'ordre croissant

    Args:
        liste_a_trie (list): liste d'element aléatoire

    Returns:
        list: la liste de depart trié dans l'ordre croissant
    """
    liste_copy=liste_a_trie.copy()
    for element in liste_a_trie:
        for i in range(len(liste_a_trie)-1):
            if liste_copy[i]>liste_copy[i+1]:
                liste_copy[i],liste_copy[i+1]=liste_copy[i+1],liste_copy[i]
    return liste_copy

##question 2
import matplotlib.pyplot as plt
import time
import random

def gen_list_rand(int_nbr:int=10,inf:int=0,sup:int=10)->list:
    """renvoi une liste des nombre int_nbr entre inf et sup 
        si rien n'est mis en parametre int_nbr=10 ,inf=0 et sup=10

    Args:
        int_nbr (int, optional): nb de valeur dans la liste. Defaults to 10.
        inf (int, optional): borne inferieur. Defaults to 0.
        sup (int, optional): borne superieur. Defaults to 10.

    Returns:
        list: _description_
    """
    retour=[]
    if inf>sup:#pour eviter un crash de random
        return []
    for i in range(int_nbr):
        retour.append(random.randint(inf,sup-1))#-1 pour avoir la borne sup non incluse
    return retour

def mesure(func:callable,iter:int,taille:list,config:int)->list:
    """la fonction calcule temps d'execution d'une func passé en parametre pour un 
       nombre d'iteration iter,et stock tout les resultat dans une liste

    Args:
        func (callable): fonction dont on veut mesurer les performance
        iter (int): nb d'iteration sur lequel on teste la fonction
        taille (list): liste qui contient les tailles des liste de test
        config (int): 1:test liste alea;2:test liste croissante;3:liste decroissante

    Returns:
        list: une liste contenant les moyenne sur les differentes tailles
    """
    liste_temps=[]
    for i in range(len(taille)):
        if config==1:# liste de nombre aleatoire
            liste=gen_list_rand(taille[i],0,taille[i]-1)
        elif config==2:# liste sorted
            liste=[item for item in range(taille[i])]
        elif config==3:# liste sorted decroissante
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

def trace_courbe(resultat1:list,resultat2:list):
    """trace les courbes des fonctions de tri 

    Args:
        resultat1 (list): liste des moyenne de la fonction 1
        resultat2 (list): liste des moyenne de la fonction 1
    """
    fig, ax = plt.subplots()
    taille=[10,100,1000]
    ax.plot(taille,resultat1, 'r*-', label='sort_list')
    ax.plot(taille,resultat2,'g*-', label='sorted')
    ax.set(ylabel='temps execution en ms', xlabel='taille des listes',title='Comparaison de fonction')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    
    plt.show()

def perf_list(func1:callable,func2:callable,taille_liste:list,nb_iteration:int)->tuple:
    """procedure qui transforme les resultat de mesure en tuple

    Args:
        func1 (callable): fonction dont on veut mesurer les performance
        func2 (callable): fonction dont on veut mesurer les performance pour comparer
        taille_liste (list): listes des tailles de liste utilisées
        nb_iteration (int): nb d'iteration de test

    Returns:
        tuple: le resultat 1,le resultat 2
    """
    result1=mesure(func1,nb_iteration,taille_liste,1)
    result2=mesure(func2,nb_iteration,taille_liste,1)
    result_final=((result1),(result2))
    return result_final

res1,res2=perf_list(sort_list,sorted,[10,100,1000],10)

trace_courbe(res1,res2)