from exo4_atelier2 import histo

#la fonction range les objets d'une liste dans 
#deux autres liste de longeur max nbemplacement et ne 
#peut pas avoir deux fois le memme object dans la memme liste

def rangement(Objets:list,nbEmplacement:int) ->tuple:
    vitrine1=[]
    vitrine2=[]
    erreur=(['placement'],['impossible'])# si aucune combinaison n'est possible
    histogramme=histo(Objets)

    for element in histogramme: #traite le cas ou 
        if element > 2:         #il y a plus de 2 occurence d'un objet
            return erreur

    if len(Objets) > (nbEmplacement* 2):#traite le cas ou l'ensemble 
        return erreur                   #ne peut pas tenir dans deux vitrines
    
    limitev1= 0 #compteur pour la limite de cpaacité de la vitrine 1
    deux_occ=[] # je crée deux liste qui separe les nombres qui se repetent
    une_occ=[]  # et ceux present en 1 exemplaire

    for i in range(len(histogramme)):   #je procede en reutilisant 
        if histogramme[i] == 1 :        #la fonction histo de l'exo 4
            une_occ.append(i)
        elif histogramme[i] == 2 :
            deux_occ.append(i)

    for i in range(len(histogramme)):
        if i in deux_occ :      # je commence par placer les nombres 
            vitrine1.append(i)  #present dans les deux vitrines
            vitrine2.append(i)  #pour eviter de deborder ou ne 
            limitev1 += 1       #pas respecter le placement
    
    for i in range(len(histogramme)):
        if i in une_occ and limitev1 < nbEmplacement:
            vitrine1.append(i)
            limitev1 +=1
        elif i in une_occ and limitev1 >= nbEmplacement:
            vitrine2.append(i)

    return vitrine1,vitrine2
            
#retourne le resulat [2,5,1,3],[2,5,4]
#Objets = [1,2,2,3,4,5,5]
#nbEmplacement = 4

#retourne le resulat erreur car il y a trois 2
#Objets = [1,2,2,2,3,4,5,5]
#nbEmplacement = 4

#retourne le resulat erreur car il a neuf elements pour 4 emplacements
#Objets = [1,2,2,3,3,4,5,5,6]
#nbEmplacement = 4

#retourne le resulat ([2, 3, 5, 1, 4], [2, 3, 5, 6])
Objets = [1,2,2,3,3,4,5,5,6]
nbEmplacement = 5

print(rangement(Objets,nbEmplacement))