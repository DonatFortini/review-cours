# la fonction prend un string et transforme le nom en majuscule
# et la premiere lettre du prenom en capital
def full_name(str_arg:str)->str:
    modif=str_arg.split(' ') #separe nom et prenom sur l'espace
    nom,prenom=modif[0],modif[1]
    new_name=nom[:].upper() #cree une copie de nom en majuscule
    new_prenom=prenom[0].capitalize()+prenom[1:] # recupere la fin de prenom 
    #et la concatene avec la premiere lettre en majuscule

    return new_name+' '+new_prenom

#retourne true si le domaine n'as pas '..' comporte un '-' et au moins un .
def domaine_valide(dom:str)->bool:
    punct=['.','-','@']
    if '-' in dom:
        i=0
        val=True
        while i <len(dom)-1:
            if dom[i]=='.' and dom[i+1]=='.':
                val=False
            elif ('.' not in dom) or dom[-1]=='.':
                val=False
            elif not(dom[i].isalpha() or dom[i].isdigit()) and (dom[i] not in punct)  :
                val=False
            i+=1  
    else: 
        val=False    
    return val

#retoutne true si le corps n'est pas vide n'as pas '..' et '.' au debut ou a la fin
def corps_valide(corps:str)->bool:
    val=True
    indesirable=['!','\\','|','"','$','%','/','(',')','=','?','@']
    if len(corps)!=0:
        if corps[0]=='.' or corps[-1]=='.':
            val=False
        else:
            i=0         
            while i <len(corps)-1:
                if corps[i]=='.' and corps[i+1]=='.':
                    val=False
                elif corps[i] in indesirable:
                    val=False
                i+=1
    else:
        val=False
    return val

#verifie si un string est une adresse mail valide 
#(1,0):valide ,(0,1) corps invalide ,(0,2) pas de @ ,(0,3) erreur domaine ,(0,4) pas de . 
def is_mail(str_arg:str)->int:
    i=0
    code=''
    while i < len(str_arg):# on separe le texte en deux a partir du @
        if str_arg[i]=='@':
            domaine=str_arg[i+1:]#pour recuperer le domaine et le corps
            corps=str_arg[:i]
        i+=1   
    
    if '@' in str_arg:
        if domaine_valide(domaine):
            if len(str_arg)==len(domaine):
                code=(0,1)
            elif corps_valide(corps):
                code=(1,0)
            else:
                code=(0,1)
        else:
            if '.' not in domaine:
                code=(0,4)
            else:
                code=(0,3)
    else:
        code=(0,2)
    return code
        
