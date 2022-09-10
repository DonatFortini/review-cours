
L=[1,2,3,4,5,6,7,8,9,10]
vide=[]
Liste=[10,2,43,3,5,6,1,20,3,2,1,2,3]
#additionne tout les chiffres de la 
#liste entre eux et retourne leur somme

def somme_1(L:list) -> int:
    somme = 0
    for i in range(len(L)):
        if  type(L[i])==str:
            i += 1
        else:
            somme += L[i]
    return somme

def somme_2(L:list) -> int:
    somme=0
    for element in L:
        if type(element)==str:
            somme+=0
        else:
            somme += element
    return somme

#pareil que les precedente sauf 
# qu'ici il faut incrementer manuellemnt l'indice

def somme_3(L:list) -> int:
    somme,i=0,0
    while i < len(L):
        if type(L[i])==str:
            i += 1
        else:
            somme += L[i]
            i += 1
    return somme

def test_exercice1 ():
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide v1: ", somme_1([]))
    print("Test liste vide v2: ", somme_1([]))
    print("Test liste vide v3: ", somme_1([]))
    #test somme 11111
    S=[1,10,100, 1000,10000]
    print("Test somme 1111 v1: ", somme_1(S))
    print("Test somme 1111 v2: ", somme_2(S))
    print("Test somme 1111 v3: ", somme_3(S))
    #test somme piegé
    S=[1,10,100, 'a',10000]
    print("Test somme piegé v1: ", somme_1(S))
    print("Test somme piegé v2: ", somme_2(S))
    print("Test somme piegé v3: ", somme_3(S))

#test_exercice1()

# ici je réutilise la fonction somme et 
# je divise par la longeur de la liste pour renvoyer la moyenne generale
def moyenne(L:list)->float:
    if len(L)==0:
        return 0
    else:
        return somme_1(L)/len(L)

#print(moyenne(L))
#print(moyenne(vide))

#les deux fonctions renvoient le nombre 
# de nombres superieur à un entier pris en parametre

def nb_sup1(L:list,e:int)->int:
    compteur = 0 
    for i in range(len(L)):
        if L[i]>e:
            compteur += 1
    return compteur

#version element

def nb_sup2(L:list,e:int)->int:
    compteur = 0 
    for element in L:
        if element>e:
            compteur += 1
    return compteur

#print(nb_sup1(L,3))
#print(nb_sup2(L,3))

# la fonction retourne la moyenne de tout les nombres superieur au parametre
def moy_sup(L:list,e:int)-> float:
    nbsup=[]
    for element in L:
        if element>e:
            nbsup.append(element)#je stocke les nombres superieur
    return moyenne(nbsup)#je fais la moyenne des nombres sup 

print(moy_sup(L,3))

#retourne la valeur maximale d'une liste

def val_max(L:list)->float:
    if len(L) != 0:
        Max=0#j'utilise un variable max qui sera remplacer par tout nombre superieur
        for element in L:
            if element > Max:
                Max=element
        return Max
    return 0

#print(val_max(Liste))

# la fonction renvois l'emplacement dans la liste de l'element max

def ind_max(L:list)->int:
    Max,ind=0,0
    for i in range(len(L)):
        if L[i]>Max:
            ind= i#sauvegarde de l'ind quand on atteind le max
            Max=L[i]
    return ind

#print(ind_max(Liste))


