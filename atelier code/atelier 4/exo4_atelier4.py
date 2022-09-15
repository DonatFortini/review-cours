import random

#extrait 5 elements aleatoirement dans la liste et les stock dans la liste retour
def extract_elements_list(list_in_which_to_choose:list, int_nbr_of_element_to_extract:int)->list:
    utilisé=[item for item in range(len(list_in_which_to_choose))] #list de tout le nombre de 0 a len
    retour=[]
    for i in range(int_nbr_of_element_to_extract):# je crée 5 nombres aleatoire et dif entre eux
        choix_alea=random.choice(utilisé)
        retour.append(list_in_which_to_choose[choix_alea])
        utilisé.remove(choix_alea)# je remove le choix pour eviter les repetitions
    return retour

def test_extra(extract_elements_list:callable):
    lst_sorted=[i for i in range(10)]
    print('Liste de départ',lst_sorted)
    sublist = extract_elements_list(lst_sorted,5)
    print('La sous liste extraite est',sublist)
    print('Liste de départ après appel de la fonction est',lst_sorted)

test_extra(extract_elements_list)

