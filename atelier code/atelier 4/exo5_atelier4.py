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

def extract_elements_list(list_in_which_to_choose:list, int_nbr_of_element_to_extract:int)->list:
    utilisé=[item for item in range(len(list_in_which_to_choose))] #list de tout le nombre de 0 a len
    retour=[]
    for i in range(int_nbr_of_element_to_extract):# je crée 5 nombres aleatoire et dif entre eux
        choix_alea=random.choice(utilisé)
        retour.append(list_in_which_to_choose[choix_alea])
        utilisé.remove(choix_alea)# je remove le choix pour eviter les repetitions
    return retour

##question 1

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

def trace_courbe_mix(resultat1:list,resultat2:list):
    resultat1=np.arange(resultat1[0],resultat1[-1],0.05)
    resultat2=np.arange(resultat2[0],resultat2[-1],0.0005)
    fig, ax = plt.subplots()
    
    ax.plot(resultat1,resultat1**5, 'r*-', label='mix_list')
    ax.plot(resultat2,resultat2,'g*-', label='shuffle')
    ax.set(xlabel='temps execution en ms', ylabel='taille des listes',title='Comparaison de fonction')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    
    plt.show()

#res1,res2=(perf_mix(mix_list,random.shuffle,[10,100,1000,10000],10))

#trace_courbe_mix(res1,res2)

##question 2

#comme mesure  mais inclus un nombre aleatoire 
#d'element a extraire de la liste pour les focntion
def mesure2(func:callable,iter:int,taille:list)->float:
    liste_temps=[]
    for i in range(len(taille)):
        temps=0
        for j in range(iter):#genere une liste de taille taille[i] pour les
            list_rando=[i for i in range(taille[i])]# iter tests à venir
            nb_alea=random.randint(0,len(list_rando)-1)
            debut=time.perf_counter()#demarre le chrono
            func(list_rando,nb_alea)#execute la fonction
            fin=time.perf_counter()#arrete le chrono 
            temps_total=fin-debut
            temps+=(temps_total)
        liste_temps.append(temps/iter)#"{:.2e}".format() pour l'ecriture
    return liste_temps #scientifique mais c'est en str

def perf_extract(func1:callable,func2:callable,taille_liste:list,nb_iteration:int)->tuple:
    result1=mesure2(func1,nb_iteration,taille_liste)
    result2=mesure2(func2,nb_iteration,taille_liste)
    result_final=((result1),(result2))
    return result_final

def trace_courbe_extra(resultat1:list,resultat2:list):
    resultat1=np.arange(resultat1[0],resultat1[-1],0.05)
    resultat2=np.arange(resultat2[0],resultat2[-1],0.0005)
    fig, ax = plt.subplots()
    
    ax.plot(resultat1,resultat1**2, 'r*-', label='extract_elemnents')
    ax.plot(resultat2,resultat2**2,'g*-', label='sample')
    ax.set(xlabel='temps execution en ms', ylabel='taille des listes',title='Comparaison de fonction')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    
    plt.show()

extrait1,extrait2=perf_extract(extract_elements_list,random.sample,[10,100,1000,10000],10)

trace_courbe_extra(extrait1,extrait2)