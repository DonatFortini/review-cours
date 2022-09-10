#la fonction copie la liste entrée en parametre ensuite remplace dans la copie les
#valeur pour les organiser en mettant les positif à droite et les negatif à gauche

def separer(L:list)->list:
    LSEP=L.copy() # je copie la liste
    fin,negatif,debut=0,0,0
    
    for i in range(len(LSEP)):
        if L[i]<0:
            negatif+=1 # je compte le nombre de negatif dans la liste

    debut,fin=0,0
    zero=negatif #ce qui permet d'initialiser le premier ou unique zero
   
    for i in range(len(L)):
        if L[i]>0:
            LSEP[-1-fin]=L[i]  #je rempli la liste a l'envers en faisant regresser l'indice
            fin+=1             # pour placer les positif de droite a gauche
        elif L[i]<0:
            LSEP[debut]=L[i]
            debut+=1 #la je remplis dans l'ordre en partant de zero
        else:
            LSEP[zero]=L[i]
            zero+=1 #en partant du nombre de negatif on peut situer le centre
    
    return LSEP

L1=[1,-1,4,3,5,-2,0,1,-3,4]
L2=[1,-2,-6,21,2,2,0,0,0,6]
L3=[-1,2,5,0,3,0,-4,5,0,-8,2]

print(separer(L1))
print(separer(L2))
print(separer(L3))

#il etait aussi possible de faire l'exercice avec 4 listes differentes 
#mais je trouvais que ça ne correspondait pas a la consigne