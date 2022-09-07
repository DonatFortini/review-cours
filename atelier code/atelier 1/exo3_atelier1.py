import math
from random import randint


def discriminant(a:float,b:float,c:float) -> float:
    if a ==0 or c==0:
        return b*b
    else:
        return b*b -4*a*c
    
def racine_u(a:float,b:float) -> float:
    return b/2*a

def racine_double(a:float,b:float,delta:float,num:int) -> float:
    if a != 0 :
        x1= (-b+math.sqrt(delta))/(2*a)
        x2= (-b-math.sqrt(delta))/(2*a)
        res=[x1,x2]
        return res[num-1]
    else:
        x1= (-b+math.sqrt(delta))
        x2= (-b-math.sqrt(delta))
        res=[x1,x2]
        return res[num-1]

def string_equa(a,b,c)->str:
    if a > 0 or a < 0:
        resultat = "{}x2".format(a)
    else:
        resultat = ""
    if b > 0:
        resultat = resultat + "+{}x".format(b)
    elif b < 0:
        resultat = resultat + "{}x".format(b)
    if c > 0:
        resultat = resultat + "+{}".format(c)
    elif c < 0:
        resultat = resultat + "{}".format(c)
    resultat = resultat.replace("1x", "x")
    if a == 0 and (b > 0 or b == 0 and c > 0):
        resultat = resultat.replace("+","",1)
    resultat = resultat + "=0"
    return resultat
    
def sol_equa(a,b,c):
    m1=string_equa(a,b,c)
    delta=discriminant(a,b,c)

    if delta > 0 :
        m3=racine_double(a,b,delta,1)
        m4=racine_double(a,b,delta,2)
        return(f"*la solution de l'equation {m1}\n a deux racine \n *x1={m3} \n *x2={m4}")
    elif delta == 0 :
        m2=racine_u(a,b)
        return(f"*la solution de l'equation {m1}\n a une racine réele {m2}")
    elif delta < 0 :
        return(f"*la solution de l'equation {m1}\n pas de racine réele")

def equation(a,b,c):
    print(sol_equa(a,b,c))




def test():
    for i in range(10):
        a,b,c=randint(-5,5),randint(-5,5),randint(-5,5)
        equation(a,b,c)

test()
