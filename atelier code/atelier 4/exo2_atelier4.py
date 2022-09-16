import random
from asserts import assert_true, assert_equal, assert_raises

def mix_list(list_to_mix:list)->list:
    """renvoit une version melangée de la liste de base

    Args:
        list_to_mix (list): liste trié de façon croisssante

    Returns:
        list: une version melangé de la liste de depart
    """
    retour=list_to_mix.copy()#je copie la liste
    utilisé=[item for item in range(len(list_to_mix))]
    #  je stock les nombre de 0 a len
    for i in range(len(list_to_mix)):
        rand=random.choice(utilisé)
        retour[i]=list_to_mix[rand]#je prend un element aleatoire de la liste 
        utilisé.remove(rand)#et l'affecte a retour[i] 
        #et je le remove pour eviter les repetitions
    return retour

def test_mix(mix_list:callable):
    lst_sorted=[i for i in range(10)]
    print(lst_sorted)
    print('Liste triée de départ',lst_sorted)
    mixed_list=mix_list(lst_sorted)
    print('Liste mélangée obtenue',mixed_list)
    print('Liste triée de départ après appel à mixList, elle doit être inchangée',lst_sorted)
    assert lst_sorted != mixed_list,"Les deux listes doivent être différente apres l'appel de mix_list"

test_mix(mix_list)