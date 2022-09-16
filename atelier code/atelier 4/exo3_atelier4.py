from random import randint

def choose_element_list(list_in_wich_to_choose:list)->int:
    """choisit un element aleatoire d'une liste

    Args:
        list_in_wich_to_choose (list): liste d'element ordonnée de façon croissante

    Returns:
        int: le nombre pris au hasard
    """
    nb_alea=randint(0,len(list_in_wich_to_choose)-1)#pour eviter le out of range
    return list_in_wich_to_choose[nb_alea]

lst_sorted=[i for i in range(10)]
print('Liste triée de départ',lst_sorted)
e1 = choose_element_list(lst_sorted)
print('A la première exécution',e1,'a été sélectionné')
e2 = choose_element_list(lst_sorted)
print('A la deuxième exécution',e2,'a été sélectionné')
assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"