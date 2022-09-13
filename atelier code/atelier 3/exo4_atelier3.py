#renvois True si le mot et le motif en pointillés sont le meme mot
def mot_correspond(mot:str,motif:str)->bool:
    if len(mot)==len(motif):#on verifie d'abord que les tailles soit similaire
        lettre_placée,point=0,0
        for i in range(len(mot)):
            if mot[i]==motif[i]:# si les lettres placées + le nb de point = len(mot)
                lettre_placée+=1#c'est que toute les lettres sont au bon endroit
            elif motif[i]=='.':
                point+=1
        return point+lettre_placée==len(mot)
    else:
        return False 

#renvois une liste [-1] si l'element n'est pas dans le mot, ses positions sinon
def presente(lettre:str,mot:str)->list:
    liste_var=[]
    if lettre in mot:
        for i in range(len(mot)):
            if lettre== mot[i]:
                liste_var.append(i)
    else:
        liste_var.append(-1)
    return liste_var

#renvois True si le mot est possible avec les lettres données
def mot_possible(mot:str,lettres:str)->bool:
    liste_var=[*mot]#decompose le mot en un tableau
    i=0
    while len(liste_var)!=0 :# si une lettre est presente dans le mot et qu'elle est dans 
        if i<len(lettres):#la variable liste_var alors on en remove une occurence
            if presente(lettres[i],mot)!=[-1] and (lettres[i] in liste_var):
                liste_var.remove(lettres[i])
                #si la liste est vide c'est que le mot est possible
            i+=1
        else:
            return False
    return True

#navigue à travers tout les mot possible du dico avec les lettres données 
# puis ne garde que ce qui on un longeur maximum 
def mot_optimaux(dico:list,lettres:str):
    liste_var,finale,max=[],[],0
    for element in dico:#on appende tout les mot possible de dico
        if mot_possible(element,lettres):
            liste_var.append(element)

    for element in liste_var:#on definit la longueur max
        if len(element)>max:
            max=len(element)
    
    for element in liste_var:#on ne garde que les mot de longueur max 
        if len(element)==max:#et possible avec les lettres donées
            finale.append(element)
    
    return finale

#voir docstring exo precedent
def dictionaire(filename:str)->list:
    file = open(filename,'r',encoding='utf-8')
    content = []
    line=file.readlines()
    for l in line :
        content.append(l.strip('\n').lower())
    file.close()
    return content

dico=dictionaire('littre.txt')

#print(mot_optimaux(dico,'hpqsbaurutackiuzoelhe'))