from random import randint


#choisit un element aleatoire d'une liste
def choose_element_list(list_in_wich_to_choose:list)->int:
    nb_alea=randint(0,len(list_in_wich_to_choose)-1)#pour eviter le out of range
    return list_in_wich_to_choose[nb_alea]

print(choose_element_list([0,2,5,3,1,6,7,22,9]))