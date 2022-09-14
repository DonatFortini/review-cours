#renvois true si le cararctère est (,[ ou {
from os import remove


def ouvrante(car:str)->bool:
    return car in ['(','[','{']

#renvois true si le cararctère est ),} ou ]
def fermante(car:str)->bool:
    return car in [')',']','}']

#renvois l'inverse de l'element car (+ pour -,( pour ),-1 pour 1 )
def reverse(car:str)->str:
    operateur=['+','-','/','*']
    if ouvrante(car):
        if car=='(':
            return ')'
        elif car== '{':
            return '}'
        else:
            return ']'
    elif fermante(car):
        if car==')':
            return '('
        elif car== '}':
            return '{'
        else:
            return '['
    elif car in operateur:
        if car=='+':
            return '-'
        elif car== '-':
            return '+'
        elif car =='*':
            return '/'
        else:
            return '*'
    elif ord(car)>=48 and ord(car)<=57:#verifie si car est un chiffre en ascii
        return -car
    else:#si car est une lettre
        return 'pas de reverse'

#renvois true si le cararctère est +,-,/ou*     
def operateur(car:str)->bool:
    return car in ['+','-','/','*']

#renvois true si le cararctère est un nombre
def nombre(car:str)->bool:
    return car.isdigit()  #la version ascii etait aussi possible

#retourne true si un element est true pour une des fonction precedente
def caractere_valide(car:str)->bool:
    return nombre(car) or operateur(car) or ouvrante(car) or fermante(car) or (car == ' ')

#verifie si tout les elements sont valides et si il y a 
#le bon nombres de parenthese ouvrantes et fermantes
def verif_parentese(expression:str)->bool:
    P=[]
    valide=True
    for i in range(len(expression)):
        if not caractere_valide(expression[i]):#on met valide a false si un seul 
            valide=False#elements est invalide
        
    
    if valide:#si la liste est valide on stock les ouvrant et fermant
        for element in expression:
            if ouvrante(element) or fermante(element):
                P.append(element)

        liste_copy=P.copy()#on copie la liste pour eviter un out of range 
        for element in liste_copy:#ou de skip des element
            if reverse(element) in P:
                P.remove(element)
                P.remove(reverse(element))
            
        return P == []#si la liste est vide c'est aue chaque element avait un reverse
    return False

exp="{[4+3]}+(2*2)"
exp2="{[4+3]}+(2*2)]"
exp3="{[4+3]}+(2*a)"

print(verif_parentese(exp))
print(verif_parentese(exp2))
print(verif_parentese(exp3))