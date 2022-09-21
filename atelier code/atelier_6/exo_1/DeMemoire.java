package atelier_6.exo_1;

public class DeMemoire extends De {
    private int memoire;

    DeMemoire(String nom,int nb_faces){
        super(nom, nb_faces);
        memoire=0;
    }

    DeMemoire(String nom){
        super(nom);
        memoire=0;
    }
    
    DeMemoire(){
        super();
        memoire=0;
    }

    public int lancer(){
        int lancer=super.lancer();
        while (lancer==memoire){
            lancer=super.lancer();
        }
        memoire=lancer;
        return lancer;
    }

    public String toString(){
        return super.toString();
    }
}
