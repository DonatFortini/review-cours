package atelier_8;
import java.lang.Math;

public class Tauren extends Personnage{
    public final int TAILLE;
    

    public Tauren(String nom,int age,int TAILLE){
        super(nom, age);
        this.TAILLE=TAILLE;
    }

    @Override
    int positionSouhaitee() {
        return getPosition()+(int)(Math.random()*TAILLE);
    }

    public String toString(){
        return "Tauren "+super.toString();
    }
}
