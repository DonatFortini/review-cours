package atelier_8;

public abstract class Personnage {
    private String nom;
    private int age;
    private int position=0;
    private Joueur proprietaire=null;

    public Personnage(String nom,int age){
        this.nom=nom;
        this.age=age;
    }

    public void deplacer(int destination ,int gain){
        this.position=destination;
        proprietaire.modifPoint(gain);
    }

    public int getPosition(){
        return this.position;
    }

    public void setPropriaitaire(Joueur j){
        proprietaire=j;
    }

    public void penaliser(int nb){
        proprietaire.modifPoint(nb);
    }

    public String toString(){
        return nom;
    }

    abstract int positionSouhaitee();
    
}
