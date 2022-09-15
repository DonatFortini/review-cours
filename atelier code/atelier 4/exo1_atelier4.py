from random import randint
#renvoi une liste des nombre int_nbr entre inf et sup 
#si rien n'est mis en parametre int_nbr=10 ,inf=0 et sup=10
def gen_list_rand(int_nbr:int=10,inf:int=0,sup:int=10)->list:
    retour=[]
    if inf>sup:#pour eviter un crash de random
        return []
    for i in range(int_nbr):
        retour.append(randint(inf,sup-1))#-1 pour avoir la borne sup non incluse
    return retour



