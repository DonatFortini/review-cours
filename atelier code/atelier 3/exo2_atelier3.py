# renvois tout les mots d'une liste d'une longueur n
def mots_Nlettres(liste:list,n:int)->list:
    liste_retour=[]
    for i in range(len(liste)):
        if len(liste[i])==n:
            liste_retour.append(liste[i])
    return liste_retour

#renvois true si le mot commence par prefixe
def commence_par(mot:str,prefixe:str)->bool:
    longeur=len(prefixe)
    return prefixe == mot[:longeur]

#renvois true si le mot finis par suffixe
def fini_par(mot:str,suffixe:str)->bool:
    longeur=len(suffixe)
    return suffixe == mot[-longeur:]

#renvois tout les mots d'une liste finnissant par suffixe
def finnissent_par(L:list,suffixe:str)->list:
    retour=[]
    for element in L:
        if fini_par(element,suffixe):
            retour.append(element)
    return retour

#renvois tout les mots d'une liste commençant par prefixe
def commencent_par(L:list,prefixe:str)->list:
    retour=[]
    for element in L:
        if commence_par(element,prefixe):
            retour.append(element)
    return retour

#renvois tout les mots commençant par prefixe,finnissant par suffixe et de longeur n
def liste_mots(lst_mot:list,prefixe:str,suffixe:str,n:int):
    retour=commencent_par(lst_mot,prefixe)
    retour=finnissent_par(retour,suffixe)#on stock le resultat dans une variable et on la 
    retour=mots_Nlettres(retour,n)#reutilise succesivement pour recuperer le resulat final
    return retour

#recupere les données d'un fichier et les transforme en liste
def dictionaire(fichier)->list:
    retour=[]
    file=open(fichier,"r",encoding='utf-8')#ouvre le fichier
    line=file.readlines() #recupere les lignes du fichier
    for l in line:#on append jusqu'a qu'il n'y est plus de ligne
        retour.append(l.strip('\n')) # pour retirer les saut de lignes 
    return retour

#print(dictionaire('littre.txt'))

def test_exercice1(func:callable):
    list_mot=['banane','bonjour','aurevoir','aventure','ordinateur','lettres','figures']
    if func(liste_mots,7)==3:
        print('succes: nb de lettres')
    else:
        print('echec: nb de lettres')
    
    


