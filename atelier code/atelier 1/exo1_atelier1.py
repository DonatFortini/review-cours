def imc(Imc:float) -> str:
    imc={"denutrition":16.4,"maigre":16.5,"normal":18.5,"surpoids":25,"ob mod":30,"ob sev":35,"ob morb":41}
    imc_inferieur=[]
    for element in imc:#je recupere toute les val du dict <= a mon Imc
        if Imc >= imc[element]:
            imc_inferieur.append(imc[element])# et je les stock dans une lsite

        if Imc < 16.4:
            return Imc , "denutrition"#cas a part car inategnable par ma boucle
    for element in imc :
        if imc_inferieur[-1]==imc[element]: #le dernier de ma liste est forcement la bonne tranche
            return Imc , element #je recuperre alors la cle associer a ma valeur


def test():
    testarr=[15,14,16.4,16.5,18,35,28,50,41,31,22,17]
    for i in range(len(testarr)):
        print(imc(testarr[i]))

test()