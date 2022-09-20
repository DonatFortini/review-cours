package atelier_6.exo_1;

public class DeImpaire extends De {
    
    public DeImpaire(String nom,int nb_faces){
        super(nom,nb_faces);
    }

    public int lancer(){
        int r=super.lancer();
        while (r%2==0){
            r=super.lancer();
        }
        return r;
    }

    public String toString(){
        return super.toString();
    }
}
