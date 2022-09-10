#la fonction renvois l'indice de 
# l'element si il s'y trouve sinon renvoi -1

def position(L:list,e:int)->int:
    if e not in L:
        return -1
    else:
        for i in range(len(L)):
            if L[i] == e:
                return i
            
#ici meme principe mais avec une boucle while
def position2(L:list,e:int)->int:
    i=0
    while  i!=len(L)-1:
        if L[i]==e:
            return i
        i+=1
    return -1
        
#renvois le nombres d'occurence de l'element e dans une liste 0 sinon
def nb_occurence(L:list,e:int)->int:
    if e not in L:
        return 0 #liste sans le e
    else:
        compteur = 0
        for element in L:
            if element == e:
                compteur += 1
        return compteur

#verifie si la liste passé en parametre est trie dans l'ordre croissant
def est_triée(L:list)->bool:
    for i in range(len(L)-1):#len-1 pour eviter le out of range si la liste est triée
        if L[i]>L[i+1]:
            return False
    return True
    
def est_triée2(L:list)->bool:
    i = 0
    while i != len(L)-1:
        if L[i] > L[i+1]:
            return False
        i += 1
    return True

#recherche en scidant succesivement la liste en deux
def position_tri(L:list,e:int)->int:
    li=L.copy()
    if (len(L) == 0) or (e not in L):#verification que e est dans la liste
        return 0

    Min=0
    Max=len(li)-1 #on cree deux borne qui serve d'indice
    while Min<=Max:
        milieu=(Min+Max)//2 #on defini un millieu
        if li[milieu]==e:
            return milieu
        elif li[milieu]>e:#si le milieu est plus grand on ne garde que 
            Max=milieu-1 #la partie de droite en faisant que Max soit le milieu -1
        else:
            Min=milieu+1# et inversement si e<li[milieu]
    return 0  

#renvoi vrai si la liste a des doublon et faux sinon
def a_repetition(L:list)->bool:
    i = 0
    t=[]
    while i != len(L):
        if L[i] not in t:
            t.append(L[i])#si L[i] est dans t c'est qu'il est un doublon
            i += 1
        else:
            return True
    return False
        

