
#verifie si le type de lettre est valide

def valide(types:str) -> bool:
    if types not in ["verte","prioritaire","ecopli","colissimo","cécograme"]:return False
    return True

#selon le dictionaire passé en parametre retourne le prix avec et sans le timbre
#et cacul aussi le prix sup si on envoit vers les DOM-TOM
def calcul_prix(tarif:dict,tarifzone:dict) :
    #partie prix de base
    choix = str(input("poids de l'envloppe "))
    while choix not in tarif:
        print("poids invalide!")
        choix = str(input("poids de l'envloppe "))
    prix=tarif[choix]#on recupere le prix avec la cle de tarif
    if "kg" in choix:#pour convertir les kilo en grammes
        poids= choix.strip('kg')#pour separer "10kg" en "10"
        poids=int(poids)#pour transformer "10" en 10
        poids*=1000
        div=poids/10# pour recuperer le coefficient de prix par tranche de 10g
    else:#si on est deja en grammes
        poids= choix.strip('g')
        poids=int(poids)
        div=poids/10
    print(f"le tarif est de {prix} £")
    # partie zone dom-tom
    reponse=input('envoyer vous vers une des zone dom-tom : O/N \n')
    if len(tarifzone) != 1:#pour le cas du colissimo car il n'y a pas de tarif zone
        if reponse == 'N':
            print( f"prix de l'envoi {prix} £")
        else:
            domtom=["Nouvelle-Calédonie", "Polynésie française", "Wallis-et-Futuna","Guyane","Guadeloupe"
            ,"Martinique", "La Réunion", "St Pierre et Miquelon"," St Barthélémy", "St-Martin"]
            print(domtom)
            zone=input("choisir la zone ")
            while zone not in domtom:
                zone=input("choisir une zone valide ")
            prix += tarifzone[zone]*div
        print(f"{prix} £")
    #partie timbre special
    timbre = input("rajouter un sticker suivi ? (+50cts) O/N ")
    if timbre == "O" or timbre == "N" :
        if timbre == "O" :
            print(f"le tarif est de {prix+0.50} £")
        else:print(f"le tarif est de {prix} ")
    else :
        print("selection invalide!")
        timbre = input("rajouter un sticker suivi ? (+50cts) O/N")

#fonction principale 
def facture():
    lettre = input("inserer un type de lettre ")
    while valide(lettre)!=True:
        lettre = input("inserer un type de lettre correct! ")

    if lettre == "verte":
        tarifpoids = {"20g":1.16,"100g":2.32,"250g":4.00,"500g":6.00,"1kg":7.50,"3kg":10.50}
        tarifzone={"Nouvelle-Calédonie":0.11, "Polynésie française":0.11 ,"Wallis-et-Futuna":0.11,"Guyane":0.05,"Guadeloupe":0.05
        ,"Martinique":0.05, "La Réunion":0.05, "St Pierre et Miquelon":0.05," St Barthélémy":0.05, "St-Martin":0.05}
        calcul_prix(tarifpoids,tarifzone)

    elif lettre == "prioritaire":
        tarifpoids = {"20g":1.43,"100g":2.86,"250g":5.26,"500g":7.89,"3kg":11.44}
        tarifzone={"Nouvelle-Calédonie":0.11, "Polynésie française":0.11 ,"Wallis-et-Futuna":0.11,"Guyane":0.05,"Guadeloupe":0.05
        ,"Martinique":0.05, "La Réunion":0.05, "St Pierre et Miquelon":0.05," St Barthélémy":0.05, "St-Martin":0.05}
        calcul_prix(tarifpoids,tarifzone)

    elif lettre == "ecopli":
        tarifpoids = {"20g":1.14,"100g":2.28,"250g":3.92}
        tarifzone={"Nouvelle-Calédonie":0.05, "Polynésie française":0.05 ,"Wallis-et-Futuna":0.05,"Guyane":0.02,"Guadeloupe":0.02
        ,"Martinique":0.02, "La Réunion":0.02, "St Pierre et Miquelon":0.02," St Barthélémy":0.02, "St-Martin":0.02}
        calcul_prix(tarifpoids,tarifzone)
    
    elif lettre == "colissimo":
        tarifzone={"toute_zone":1}
        tarifpoids = {"500g":8.35,"1kg":11.20,"2kg":14.10,"5kg":23.65,"10kg":37.50,"15kg":75.85,"30kg":87.40}
        calcul_prix(tarifpoids,tarifzone)
       
facture()

