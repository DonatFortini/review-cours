package atelier_8;

public class Humain extends Personnage {
    private static int nbDeplacement;
    private static int niveau;

    public Humain(String nom,int age){
        super(nom, age);
        niveau=1;
        nbDeplacement=0;
    }

    public void deplacer(int destination,int gain){
        super.deplacer(destination, gain);
        nbDeplacement++;
        if(nbDeplacement%2==0 && niveau<3){
            niveau=nbDeplacement/2;
        }
    }

    @Override
    int positionSouhaitee() {
        return getPosition()+niveau*nbDeplacement;
    }

    public String toString(){
        return "Humain "+super.toString();
    }
}
