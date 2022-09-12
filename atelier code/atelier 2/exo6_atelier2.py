#retourne true si l'element est dans la liste

def present(L:list,e:int)->bool:
    return e in L

def test_present(func_present:callable) -> None:
    liste_10_val=[1,2,4,4,66,75,4,3,2,34]
    if func_present([],0):
        print("ECHEC: test liste vide")
    else:
        print( "SUCCES : test liste vide")
       

    if func_present(liste_10_val,1):
        print("SUCCES : test debut")
    else:
        print("ECHEC : test debut")
   
    
    if func_present(liste_10_val,34):
        print("SUCCES : test fin")
    else:
        print("ECHEC : test fin")
    

    if func_present(liste_10_val,66):
        print("SUCCES : test milieu")
    else:
        print("ECHEC : test milieu")
   

    if not func_present(liste_10_val,5):
        print("SUCCES : test absence")
    else:
        print("ECHEC : test absence")

#test_present(present)
#print("\n")

##Question 3

#VERSION 1
# le return arrete la fonction et donc la bloque 
#def present1 (L, e) :
    #for i in range (0, len(L), 1) :
        #if (L[i] == e) :
            #return(True)
        #else : --> ce else ne sert que a casser la fonction
            #return (False) 
    #return (False)

#VERSION 1 amelioré 
def present1 (L, e) :
    for i in range (len(L)) :
        if (L[i] == e) :
            return(True)
    return (False)
        
#VERSION 2
#l'erreur est que le else change la valeur de b a chaque element de L
#def present2 (L, e) :
    #b=True
    #for i in range (0, len(L), 1) :
       # if (L[i] == e) :
       #     b=True
       # else :
      #      b=False
    #return (b)

#VERSION 2 amelioré 
def present2 (L, e) :
    b=False # il faut alors demarer a false
    for i in range (len(L)) :
        if (L[i] == e) :
            b=True
    return (b)

#VERSION 3 
#l'erreur est que la fonction s'arrete apres le premier envoi a cause de return
#def present3 (L, e) :
   # b=True -> pas utilisé
    #for i in range (0, len(L), 1) :
    #    return (L[i] == e) -> l'arrete a la premiere iteration 

#VERSION 3 amelioré
def present3 (L, e) :
    b=True
    for i in range (len(L)) :
        if (L[i] == e):
            return b

#VERSION 4
# les erreurs : pas d'incrementation de i,le and b dans le while
#def present4 (L, e) :
#   b=False
#   i=0
#    while (i<len(L) and b) :
#        if (L[i] == e) :
#            b=True
#    return (b)

#VERSION 4 amelioré
def present4 (L, e) :
    b=False
    i=0
    while  i<len(L) :
        if (L[i] == e) :
            b = True
        i += 1
    return b

#print("test p1")
#test_present(present1)
#print("\n")
#print("test p2")
#test_present(present2)
#print("\n")
#print("test p3")
#test_present(present3)
#print("\n")
#print("test p4")
#test_present(present4)

##Question 4

# renvoi toutes les  positions de e dans L
def pos(L:list,e:int)->list:
    position=[]
    if e in L:
        for i in range(len(L)):
            if L[i] == e:
                position.append(i)
        return position
    return position

#print(pos([3,4,5,7,2,7], 7)) 

def test_pos(func_Pos:callable) ->None :
    liste_10_val=[1,2,3,7,4,6,2,8,21,12]
    if func_Pos([],0) != []:
        print("ECHEC: test liste vide")
    else:
        print( "SUCCES : test liste vide")
       

    if func_Pos(liste_10_val,1) == [0]:
        print("SUCCES : test debut")
    else:
        print("ECHEC : test debut")
   
    
    if func_Pos(liste_10_val,12) == [9]:
        print("SUCCES : test fin")
    else:
        print("ECHEC : test fin")
    

    if func_Pos(liste_10_val,6) == [5]:
        print("SUCCES : test milieu")
    else:
        print("ECHEC : test milieu")
   

    if func_Pos(liste_10_val,5) == []:
        print("SUCCES : test absence")
    else:
        print("ECHEC : test absence")

#VERSION 1
def pos1(L, e) :
    Lres = list(L)
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres += [i]
    return Lres

# VERSION 2
def pos2(L, e) :
    Lres = list(L)
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres[i] = i
    return Lres

# VERSION 3
def pos3(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres.append(i)
    return Lres

# VERSION 4
def pos4(L, e) :
    nb= L.count(e)
    Lres = [0]*nb #-> on pourrait optimiser en  faisant une copie de la liste
    j=0 #-> ne sert à rien
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres[j]= i
    return Lres




test_pos(pos)
print("\n")
print("test p1")
test_pos(pos1)
print("\n")
print("test p2")
test_pos(pos2)
print("\n")
print("test p3")
test_pos(pos3)
print("\n")
print("test p4")
test_pos(pos4)