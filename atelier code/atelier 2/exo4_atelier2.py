import matplotlib.pyplot as plt
#je reeutilise deux fonction des precedent exercice pour compter les occurences
# et determiner la valeur max 

def val_max(L:list)->float:
    if len(L) != 0:
        Max=0#j'utilise un variable max qui sera remplacer par tout nombre superieur
        for element in L:
            if element > Max:
                Max=element
        return Max
    return 0

def nb_occurence(L:list,e:int)->int:
    if e not in L:
        return 0 #liste sans le e
    else:
        compteur = 0
        for element in L:
            if element == e:
                compteur += 1
        return compteur

## Question 1

#la fonction initialise H a la valeur max de la liste F +1 pour que H soit indicé
# de 0 à valmax puis compte le nombre d'ocurence de chaque chiffres dans H
def histo(F:list)->list:
    max_valeur=val_max(F)+1 #+1 pour avoir l'indiçage correct
    H=[0]*max_valeur #initialise la liste
    for element in F:
        valeur=nb_occurence(F,element)#on recupere le nb d'occurence
        H[element]=valeur #et les place au bon emplacement dans H
    return H

# si l'histograme de la fonction a une valeur qui presente 
# plus d'une fois alors la fonction renvois false
def est_injective(F:list)->bool:
    H=histo(F)
    for element in H :
        if element > 1:
            return False
    return True

#definie si une fonction est surjective c-a-d si tout ses 
#elements sont tout egaux à 1 ou plus
def est_surjective(F:list)->bool:
    H=histo(F)
    for element in H :
        if element == 0: # il faut que tout les element soit = ou > à 1
            return False # donc si un seul est = à 0 on retourne false
    return True

#la fonction est une fusion des deux precedente. Renvois true si bijective
def est_bijective(F:list)-> bool:
    if est_surjective(F) and est_injective(F):
        return True
    return False

## Question 2

# la fonction print un histogramme de la fonction F
def tracé_histo(F:list) :
    print("TEST HISTOGRAME")
    print(f"F={F}\nHISTOGRAME\n")
    H=histo(F)
    
    for i in range(val_max(H)): # je commence par la boucle de hauteur
        for j in range(len(H)): # et la seconde s'occupe de la longeur
            if (H[j] >= val_max(H)-i) : # la condition permet de print les colonne
                print("  #  ",end='') #ligne par lignes un element par un 
            else:
                print('     ',end='')   #je print pour cree les espaces entre les valeurs
        print() #pour casser le end line

    for c in range(len(H)):
        print(f'|-{c}-|',end='')
    print() #pour casser le end line

#F=[1,1,1,1,3,4,6,6,6,7,8,9]
#F=[3,0,6,7,4,2,1,5]
F=[9,2,5,4,4,2,0,2,8]
#tracé_histo(F)

## Question 3

#la fonction renvoi un histogramme de la fonction F
def test_histo(F:list):
    plt.style.use('fivethirtyeight') #puremment graphique
    bin=[item for item in range(len(F))] #genere une liste de 0 a valmax
    plt.hist(F,bins=bin,edgecolor='black')#separe les colonnes avec des cotés coloré
    plt.title('Histogramme avec matplotlib')#titre de l'histogramme
    plt.show()#pour print le graphique

#test_histo(F)



