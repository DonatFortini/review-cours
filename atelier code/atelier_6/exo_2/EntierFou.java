package atelier_6.exo_2;

import java.util.Random;

public class EntierFou extends Entier {
    int niv_folie;
    
    public EntierFou(int inf,int sup,int valeur ,int niv_folie){
        super(inf, sup, valeur);
        this.niv_folie=niv_folie;
    
    }

    public void incremente(){
        Random rand=new Random();
        int r=rand.nextInt(0,this.niv_folie);
        super.incremente(r);
    }

    public String toString(){
        return super.toString();
    }
}
