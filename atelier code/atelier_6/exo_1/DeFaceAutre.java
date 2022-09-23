package atelier_6.exo_1;



public class DeFaceAutre extends De {
    private static final String[] LISTE_MOT={ "Gagné", "Perdu", "Relancez", "Passez votre tour" };
    private int faces=LISTE_MOT.length;

    public DeFaceAutre(String nom){
        super(nom);
        this.setNbFaces(faces);
    }

    public int lancer(){
        return  super.lancer();
    }

    public String toString(){
        super.toString();
        return LISTE_MOT[lancer()];
    }
}
