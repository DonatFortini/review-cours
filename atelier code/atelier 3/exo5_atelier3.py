#renvois true si le cararctère est (,[ ou {
def ouvrante(car:str)->bool:
    return car in ['(','[','{']

#renvois true si le cararctère est ),} ou ]
def fermante(car:str)->bool:
    return car in [')',']','}']

#renvois l'inverse de car si c'est ( ou [ ou { , sinon renvois car 
def reverse(car:str)->str:
    operateur=['+','-','/','*']
    if ouvrante(car):
        if car=='(':
            return ')'
        elif car== '{':
            return '}'
        else:
            return ']'
    elif fermante(car) or car in operateur:
        return car
    elif ord(car)>=48 and ord(car)<=57:#verifie si car est un chiffre en ascii
        return car
    else:#si car est une lettre
        return 'pas de reverse'

#renvois true si le cararctère est +,-,/ou*     
def operateur(car:str)->bool:
    return car in ['+','-','/','*']

#renvois true si le cararctère est un nombre
def nombre(car:str)->bool:
    return car.isdigit()  #la version ascii etait aussi possible

def caractere_valide(car:str)->bool:
    return nombre(car) or operateur(car) or ouvrante(car) or fermante(car) or (car == ' ')

def verif_parentese(expression:str)->bool:
    P=[]
    valide=False
    for i in range(len(expression)):
        if caractere_valide(expression[i]):
            valide=True
    
    if valide:
        for element in expression:
            if ouvrante(element):
                P.append(element)
        