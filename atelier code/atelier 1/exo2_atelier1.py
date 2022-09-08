#verifie qu'une année est bissextile
def bissextile(année:int) -> bool:
    while année%1!=0:#pour verifier que l'année est bien un entier
        print("la proposition n'est pas un entier\n")
        année=input("nouvelle proposition : ")
    if année%4==0 :
        if (année%100==0 and année%400==0) or (année%100!=0 and année%400!=0):
            return True
    return False

def test():
    testarr=[2000,1996,1584,1900,1600,1345,1200,144,2020,1800]
    for i in range(len(testarr)):
        print(bissextile(testarr[i]))

test()