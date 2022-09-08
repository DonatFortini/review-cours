from datetime import date
from random import randint


def bissextile(année:int) -> bool:
    while année%1!=0:
        print("la proposition n'est pas un entier\n")
        année=input("nouvelle proposition : ")
    if année%4==0 :
        if (année%100==0 and année%400==0) or (année%100!=0 and année%400!=0):
            return True
    return False

#verifie si la date est possible dans un calendrier
def date_est_valide(jour:int,mois:int,année:int) -> bool:
    mois31=[1,3,5,7,8,10,12]#je divise les mois en deux groupe et laisse
    mois30=[4,6,9,11]# à part fevrier pour traiter ses deux cas separement
    if (jour or mois) !=0:
        if mois in mois31:
            if jour>31: return False
        elif mois in mois30:
            if jour>30: return False
        if mois==2:#cas fevrier
            if bissextile(année):
                if jour>29: return False
            else:
                if jour>28: return False
        if mois>12 or année<0:return False
    return True

# permet de retourner une date ecrite en int en format date
def saisi_date_de_naissance(jour:int,mois:int,année:int) -> date:
    if date_est_valide(jour,mois,année):#on valide la date, si oui on la formatte
        return date(année,mois,jour)
    else:
        ok=False
        while ok==False:#sinon tant qu'une date valide n'est pas saisie on redemande
            nouvelle_date=input("date valide svp (format j,m,a) ")
            if not "," in nouvelle_date:#pour le cas on qqun ecrivais 12122021 ou 12/12/2021
                nouvelle_date=input("date valide svp (format j,m,a) ")
            
            jour,mois,année=nouvelle_date.split(',')#on recupe les inputs en str
            jour,mois,année=int(jour),int(mois),int(année)#on les remet en int
            if date_est_valide(jour,mois,année):ok=True
        return date(année,mois,jour)
            
#par difference avec la date d'auj ,retourne l'age
def age(date_de_naissance:date)->int :
    comp=date.today()#date d'aujourd'hui
    x=str(comp-date_de_naissance)#on recupere le nombre de jours en str
    x=x.split()
    x=x[0]
    x=int(x)/365#on le divise par un an en jours
    return int(x)#on l'arrondit au supperieur grace a int
    
def est_majeur(date_de_naissance:date)-> bool:
    return age(date_de_naissance)>=18
        

def acces(date_de_naissance:date):
    if est_majeur(date_de_naissance):
        print(f"bonjour vous avez {age(date_de_naissance)} ans vous pouvez rentrer")
    else:
        print(f"bonjour vous avez {age(date_de_naissance)} ans  vous ne pouvez pas rentrer")   



def test():
    for i in range(10):
        jour,mois,année=randint(1,100),randint(1,12),randint(1950,2020)
        date_de_naissance=saisi_date_de_naissance(jour,mois,année)
        print(date_de_naissance)
        acces(date_de_naissance)

test()
