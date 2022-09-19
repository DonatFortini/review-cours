##question 1
import random

def stupid_sort(list_to_sort:list)->list:
    """tri inutile qui melange aleatoirement la liste jusqu'a quelle soit triée 

    Args:
        list_to_sort (list): liste à trier

    Returns:
        list: la liste de depart triée
    """
    list_var=list_to_sort.copy()# on copie pour ne pas toucher a la liste d'origine
    while list_var != list_var.sort():
        random.shuffle(list_var)
    return list_var

##question 2

def tri_insertion(list_to_sort:list)->list:
    """tri en inserant une valeur a des endroit specifique de la liste

    Args:
        list_to_sort (list): liste à trier

    Returns:
        list: la liste de depart triée
    """
    liste_var=list_to_sort.copy()
    for i in range(1,len(liste_var)):
        en_cours = liste_var[i]
        j = i
    
        while j>0 and liste_var[j-1]>en_cours:
            liste_var[j]=liste_var[j-1]
            j = j-1
        liste_var[j]=en_cours
    return liste_var

##question 3

def tri_selection(list_to_sort:list)->list:
    """trie la liste en comparant les element au minimum

    Args:
        list_to_sort (list): liste à trier

    Returns:
        list: la liste de depart triée
    """
    list_var=list_to_sort.copy()
    for i in range(len(list_var)-1):
        min=i
        for j in range(i+1,len(list_var)):
            if list_var[j]<list_var[min]:
                min=j   
        if min!=i:
            list_var[i],list_var[min]=list_var[min],list_var[i]
    return list_var

## question 4

def tri_bulle(list_to_sort:list)->list:
    """echange les element successivement jusqu'a que la liste soit triée

    Args:
        list_to_sort (list): liste à trier

    Returns:
        list: la liste de depart triée
    """
    list_var=list_to_sort.copy()
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(list_var) - passage):
            if list_var[en_cours] > list_var[en_cours + 1]:
                permutation = True
                # On echange les deux elements
                list_var[en_cours], list_var[en_cours + 1] = \
                list_var[en_cours + 1],list_var[en_cours]
    return list_var 

## question 5

def tri_fusion(list_to_sort:list)->list:
    """melange des slice de liste jusqu'a retourner une lsite triée

    Args:
        list_to_sort (list): liste à trier

    Returns:
        list: la liste de depart triée
    """
    list_var=list_to_sort.copy()
    if  len(list_var) <= 1: 
        return list_var
    pivot = len(list_var)//2
    list_var1 = list_var[:pivot]
    list_var2 = list_var[pivot:]
    gauche = tri_fusion(list_var1)
    droite = tri_fusion(list_var2)
    fusionne = fusion(gauche,droite)
    return fusionne

def fusion(list_to_sort1:list,list_to_sort2:list)->list:
    """trie les liste en parametre puis les fusionne

    Args:
        list_to_sort1 (list): liste à trier
        list_to_sort2 (list): liste à trier

    Returns:
        list: une fusion des liste en parametre triée
    """
    list_var1,list_var2=list_to_sort1.copy(),list_to_sort2.copy()
    indice_list_var1 = 0
    indice_list_var2 = 0    
    taille_list_var1 = len(list_var1)
    taille_list_var2 = len(list_var2)
    list_var_fusionne = []
    while indice_list_var1<taille_list_var1 and indice_list_var2<taille_list_var2:
        if list_var1[indice_list_var1] < list_var2[indice_list_var2]:
            list_var_fusionne.append(list_var1[indice_list_var1])
            indice_list_var1 += 1
        else:
            list_var_fusionne.append(list_var2[indice_list_var2])
            indice_list_var2 += 1
    while indice_list_var1<taille_list_var1:
        list_var_fusionne.append(list_var1[indice_list_var1])
        indice_list_var1+=1
    while indice_list_var2<taille_list_var2:
        list_var_fusionne.append(list_var2[indice_list_var2])
        indice_list_var2+=1
    return list_var_fusionne

## question 6

def tri_base(list_to_sort:list)->list:
    """on cherche d'abord le max de la liste puis on le decompose en exposant
    qui sera la borne max puis pour i a Max on tri lea liste successivement selon 
    l'ordre croissant: des unitées,des dizaines puis des centaines
    et retourne la liste triée dans l'ordre croissant

    Args:
        list_to_sort (list): liste à trier

    Returns:
        list: la liste de depart triée
    """
    list_var=list_to_sort.copy()
    
    def tri(list_var:list,exposant)->list:
        l_var=[[],[],[],[],[],[],[],[],[],[]]# on y stockera les nombre selon le iemme chiffre de 0 à 9
        resultat=[]
        #l'incrementation de l'expo va permetre de faire unité puis dizaines,puis centaine
        for i in range(len(list_var)):
            l_var[(list_var[i]%10**(exposant+1))//10**exposant].append(list_var[i])
        for h in range(len(l_var)):
            resultat+=l_var[h]#on concatene pour recup une

        return resultat

    Max= max(list_to_sort)
    i=0
    while Max %10**i != Max:
        i+=1
    Max=i

    for i in range(Max):
        list_var=tri(list_var,i)
    
    

    return list_var

###EXERCICE 8

import matplotlib.pyplot as plt
import time

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

def mesure(func:callable,iter:int,taille:list,config:int)->float:
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
        if config==1:
            liste=gen_list_rand(taille[i],0,taille[i]-1)
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

def trace_courbe(res2:list,res3:list,res4:list,res5:list,res6:list,res7:list):
    """trace les courbes des fonctions de tri 

    Args:
        #res1 (list): liste des moyenne de la fonction 1
        res2 (list): liste des moyenne de la fonction 2
        res3 (list): liste des moyenne de la fonction 3
        res4 (list): liste des moyenne de la fonction 4
        res5 (list): liste des moyenne de la fonction 5
        res6 (list): liste des moyenne de la fonction 6
        res6 (list): liste des moyenne de la fonction 7
    """
    fig, ax = plt.subplots()
    taille=[10,100,500,1000,1500]
    #ax.plot(taille,res1, 'r*-', label='stupid')#impossible de demarrer avec lui
    ax.plot(taille,res2,'g*-', label='inser')
    ax.plot(taille,res3,'b*-', label='select')
    ax.plot(taille,res4,'y*-', label='bulle')
    ax.plot(taille,res5,'m*-', label='fusion')
    ax.plot(taille,res6,'k*-', label='base')
    ax.plot(taille,res7,'r*-', label='sorted')
   
    ax.set(ylabel='temps execution en ms', xlabel='taille des listes',title='Comparaison de fonction')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    
    plt.show()

taille=[10,100,500,1000,1500]
#res1=mesure(stupid_sort,5,taille,1) le tri stupide est tellement long qu'il fait tout crash
res2=mesure(tri_insertion,50,taille,1)
res3=mesure(tri_selection,50,taille,1)
res4=mesure(tri_bulle,50,taille,1)
res5=mesure(tri_fusion,50,taille,1)
res6=mesure(tri_base,50,taille,1)
res7=mesure(sorted,50,taille,1)

#config 1 
trace_courbe(res2,res3,res4,res5,res6,res7)
