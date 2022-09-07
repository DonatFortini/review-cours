import random

# la fonction evalue les differentes possibilitées et renvoie les scores apres les avoir modifiés 

def a_gagné(choixj1:str,choixj2:str,scorej2:int,scorej1:int) -> tuple:
    if choixj1 == "papier" and choixj2 == "ciseaux":
        scorej2 += 1
        return scorej1,scorej2
    elif choixj1 == "papier" and (choixj2 == "pierre" or choixj2 == "puit"):
        scorej1 += 1
        return scorej1,scorej2 
    elif choixj2 == choixj1:return scorej1,scorej2

    elif choixj1 == "ciseaux" and (choixj2 == "pierre" or choixj2 == "puit"):
        scorej2 += 1
        return scorej1,scorej2
    elif choixj1 == "ciseaux" and choixj2 == "papier":
        scorej1 += 1
        return scorej1,scorej2
    elif choixj2 == choixj1:return scorej1,scorej2
    
    elif choixj1 == "pierre" and (choixj2 == "papier" or choixj2 == "puit"):
        scorej2 += 1
        return scorej1,scorej2
    elif choixj1 == "pierre" and choixj2 == "ciseaux":
        scorej1 += 1
        return scorej1,scorej2
    elif choixj2 == choixj1:return scorej1,scorej2

    elif choixj1 == "puit" and choixj2 == "papier":
        scorej2 += 1
        return scorej1,scorej2
    elif choixj1 == "puit" and (choixj2 == "ciseaux" or choixj2 == "pierre"):
        scorej1 += 1
        return scorej1,scorej2
    elif choixj2 == choixj1:return scorej1,scorej2

#la fonction return le choix si il est correct (ergo, dans la liste) et false sinon
def correct(choix:str) :
    choix=choix.lower() #pour remettre tout en minuscule
    if choix in ["pierre", "papier", "ciseaux","puit"] : return choix
    return False
    
#boucle de jeu

cpo = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )
while cpo != "O" and cpo != "N":
        print("Je n'ai pas compris votre réponse")
        cpo = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )

#la variable solo sert a determiner 
# si le joueur a choisis de jouer contre l'ordi ou non, true si ordi false si multi

solo = True
joueur1 = input("Quel est votre nom ? ")

if cpo == 'O':
    joueur2 = 'Machine'
    print("Bienvenu ", joueur1 , " nous allons jouer ensemble \n")
else:
    solo = False 
    joueur2 = input("Quel est votre nom ? ")
    print("Bienvenu " , joueur1 , " et " , joueur2 , " nous allons jouer ensemble \n")

#initialisation des scores et du nombre de tour
scorej2,scorej1,nbtour = 0,0,0

while nbtour < 5:
    nbtour += 1 
    choixj1 = str(input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux,puit): ".format(nom = joueur1)))
    while correct(choixj1) == False:
        choixj1 = str(input("Entrer une reponse valide : "))
    if solo:#tour de j2 si il est l'ordi
        choixj2 = ['papier','pierre','ciseaux','puit'][random.randint(0, 3)]
    else:#tour de j2 si j2 est un joueur
        choixj2 = str(input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux,puit): ".format(nom = joueur2)))
        while correct(choixj2) == False:
            choixj2 = str(input("Entrer une reponse valide : "))
    scorej1,scorej2 = a_gagné(choixj1,choixj2,scorej2,scorej1)
    print ("score ",scorej1," - ",scorej2)

if scorej2 > scorej1:
    print(joueur2," a gagné ",scorej2," à ",scorej1 )
elif scorej1 > scorej2:
    print(joueur1, " a gagné ",scorej1," à ",scorej2 )
else:
    print("egalité")