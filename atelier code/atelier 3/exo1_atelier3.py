
def full_name(str_arg:str)->str:
    modif=str_arg.split(' ')
    nom,prenom=modif[0],modif[1]
    new_name=nom[:].upper()
    new_prenom=prenom[0].capitalize()+prenom[1:]

    return new_name+' '+new_prenom

def domaine_valide(dom:str)->bool:
    i=0
    val=True
    while i <len(dom)-1:
        if dom[i]=='.' and dom[i+1]=='.':
            val=False
        elif ('.' not in dom) or dom[-1]=='.':
            val=False
        i+=1      
    return val

def corps_valide(corps:str)->bool:
    val=True
    if len(corps)!=0:
        if corps[0]=='.' or corps[-1]=='.':
            val=False
        else:
            i=0         
            while i <len(corps)-1:
                if corps[i]=='.' and corps[i+1]=='.':
                    val=False
                i+=1
    else:
        val=False
    return val

def is_mail(str_arg:str)->int:
    i=0
    code=''
    while i < len(str_arg):
        if str_arg[i]=='@':
            domaine=str_arg[i+1:]
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
        
str_variable2test = '@univ-corse.fr'

print(is_mail(str_variable2test))