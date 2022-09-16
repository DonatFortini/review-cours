from random import randint

def gen_list_rand(int_nbr:int=10,inf:int=0,sup:int=10)->list:
    """renvoi une liste des nombre int_nbr entre inf et sup 
        si rien n'est mis en parametre int_nbr=10 ,inf=0 et sup=10

    Args:
        int_nbr (int, optional): nb de valeur dans la liste. Defaults to 10.
        inf (int, optional): borne inferieur. Defaults to 0.
        sup (int, optional): borne superieur. Defaults to 10.

    Returns:
        list: _description_
    """
    retour=[]
    if inf>sup:#pour eviter un crash de random
        return []
    for i in range(int_nbr):
        retour.append(randint(inf,sup-1))#-1 pour avoir la borne sup non incluse
    return retour



