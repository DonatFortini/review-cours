package atelier_6.exo_1;

import java.util.Random;

public class De {
    private final String nom;
    private int nbFaces=6;
    private static final int INF=3;
    private static final int SUP=120;
    private static int nbDe=0;
    private static Random rand =new Random();

    public De(String nom,int nbFaces){
        this.nom=nom;
        setNbFaces(nbFaces);
        nbDe+=1;
    }

    public De(String nom){
        this(nom, 6);
    }

    public De(){
        this(("De"+nbDe));
    }

    public int getNbFaces(){
        /**
         * @return renvoit le nombre de faces d'un dé
         */
        return this.nbFaces;
    }

    public void setNbFaces(int modif){
        /**
         * modifie le nombre de faces d'un dé
         * @param modif le nouveau nombre de faces
         */
        if (modif>INF && modif<SUP){
            this.nbFaces=modif;
        }
        else{
            System.err.println("nombre pas entre les borne");
        }
    }

    public String getNom(){
        /**
         * @return renvoit le nom d'un dé
         */
        return this.nom;
    }

    public int lancer(){
        /**
         * renvoit un nombre aleatoire generer entre 0 et le nbFaces d'un dé
         * @return renvoit un nombre aleatoire 
         */
        return rand.nextInt(1,this.nbFaces+1);
    }

    public int lancer(int nb){
        int max=0;
        int lancer=rand.nextInt(1,this.getNbFaces()+1);
        for(int i=0;i<nb;i++){
            if (lancer== nbFaces){
                return lancer;
            }
            else if(lancer >max){
                max=lancer;
            }   
        }
        return max;
    }

    public String toString(){
        return "Dé : "+nom+" nombre de faces: "+nbFaces;
    }

    public boolean equals(Object autre){
        if(autre!=null && autre instanceof De){
            De objectDe=(De)autre;
            return (this.nom.equals(objectDe.nom) && this.nbFaces==objectDe.nbFaces);
        }
        return false;
    }

}

