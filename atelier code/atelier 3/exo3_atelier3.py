import random
##question 1

#renvois une liste des positions de ch dans un mots
def places_lettre(ch:str,mot:str)->list:
    retour=[]
    for i in range(len(mot)):
        if ch == mot[i]:
            retour.append(i)
    return retour

def test_place():
    i=str(input("ecriver une lettre et un mot (stop pour stop) "))
    modif=i.split(',')
    lettre,mot=modif[0],modif[1]
    while (lettre or mot) != ('stop' or 'STOP'):
        print(places_lettre(lettre,mot))
        i=str(input("ecriver une lettre et un mot (stop,exit pour stop) "))
        modif=i.split(',')
        lettre,mot=modif[0],modif[1]
    print('fin')

#test_place()

##question 2

#selon les valeurs dans pos, renvois un mot ou 
#les position sont des lettre et le reste est '_' 
def outpout_string(mot:str,lpos:list)->str:
    retour=''
    if len(mot) != len(lpos):
        for i in range(len(mot)):
            if i in lpos:
                retour+=mot[i]
            else:
                retour+='_'
        return retour 
    return mot

#question 4
#cree une liste a partir des donnée d'un fichier
def build_list(filename:str)->list:
    file = open(filename,'r',encoding='utf-8')#ouvre le fichier et l'encode en utf-8
    content = []
    line=file.readlines()#recupere toutes les lignes d'un fichier
    for l in line :
        content.append(l.strip('\n').lower())#enleve les saut de ligne et met tout en minuscule
    file.close() #ferme le fichier
    return content

## question 3

#verifis si l'input n'est ni un nombre ni deux lettres ni n'as deja été dit
def input_valide(inp:str,deja_dit:list):
    while inp in deja_dit:
        while (len(inp)!=1 or inp.isdigit()) and inp in deja_dit :
            print(deja_dit)
            inp=str(input('inserer une lettre '))
   
    while len(inp)!=1 and not(inp.isdigit()) :
        print(deja_dit)
        inp=str(input('inserer une lettre '))
    return True

#affiche le pendu selon l'avancé de compteur
def pendu_af(compteur:int):
    if compteur ==1:
        print('|---   ')
    elif compteur ==2:
        print('|---   ')
        print('|   O  ')
    elif compteur ==3:
        print('|---   ')
        print('|   O  ')
        print('|   I  ')  
    elif compteur == 4:
        print('|---   ')
        print('|   O  ')
        print('|   I  ')  
        print('|  /\\ ')
    elif compteur == 5:
        print('|---   ')
        print('|   O  ')
        print('|   I  ')  
        print('|  /\\ ')
        print('|------')

#boucle principale
def run_game():
    liste_mot=build_list("capitales_pays.txt")
    mot_choisis=random.choice(liste_mot)
    print(outpout_string(mot_choisis,[]))
    pendu=str(input('inserer une lettre '))
    compteur,nbcoup=0,0
    deja_dit=[]

    if input_valide(pendu,deja_dit):
        if places_lettre(pendu,mot_choisis)==[]:
            compteur += 1
    deja_dit.append(pendu)       

    nbcoup+=1
    pendu_af(compteur)
    pos=places_lettre(pendu,mot_choisis)
    a_deviner=outpout_string(mot_choisis,pos)

    while (mot_choisis != a_deviner) and (compteur != 5):
        print(f'{a_deviner}\n')
        print(deja_dit)
        pendu = str(input('inserer une lettre '))
        if input_valide(pendu,deja_dit):
            if places_lettre(pendu,mot_choisis)==[]:
                compteur += 1
            deja_dit.append(pendu)
            nbcoup+=1
            pos+=places_lettre(pendu,mot_choisis)
            a_deviner=outpout_string(mot_choisis,pos)

            pendu_af(compteur)
    if a_deviner==mot_choisis:
        print(f'vous avez gagner en {nbcoup} coups')
    else:
        print(f'perdu!')
        
#run_game()

##question 5
#renvois le mot le plus long d'une liste
def mot_leplus(liste:list)->int:
    max=0
    for i in range(len(liste)):
        if len(liste[i])>max:
            max=len(liste[i])
    return max
   
def mots_Nlettres(liste:list,n:int)->list:
    liste_retour=[]
    for i in range(len(liste)):
        if len(liste[i])==n:
            liste_retour.append(liste[i])
    return liste_retour

#pareil que la precedente mais creer un dictionnaire avec la longeur en clé et les pays en valeur
def build_list2(filename:str)->dict:
    file = open(filename,'r',encoding='utf-8')
    content ={}
    listevar=[]
    line=file.readlines()
    for l in line :
        listevar.append(l.strip('\n').lower())#enleve les saut de ligne et met tout en miniscule
    for i in range(mot_leplus(listevar)):
        content[i]=mots_Nlettres(listevar,i)#stock les valeur dans le dico selon leur longueur
    
    for i in range(len(content)):#supprime les cle avec aucune valeur
        if content[i]==[]:
            del content[i]
    file.close()
    return content

#choisis un mot au hasard dans un dictionnaire ou longueur = n
def select_word(sorted_word:dict,word_len:int)->str:
    if word_len in sorted_word:
        return random.choice(sorted_word[word_len])#on prend un mot aléatoire la ou clé=n
    else:
        return (f'aucun pays avec la longeur {word_len}')

#selon le niveau de difficulté,renvois une liste comprenant des pays 
# avec des noms de plus en plus long
def niveau_dif(dico:dict)->list:
    choix=str(input('choix de la diff 1:facile,2:moyen,3:difficile'))
    retour=[]
    if choix == 'facile':
        for i in range(7):
            if i in dico:
                retour+=dico[i]
    elif choix == 'moyen':
        for i in range(6,9):
            if i in dico:
                retour+=dico[i]
    elif choix == 'difficile':
        for i in range(8,len(dico)):
            if i in dico:
                retour+=dico[i]

    return retour



