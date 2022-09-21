package atelier_6.exo_1;

public class DePipe extends De{
    private final int BORNE ;

    public DePipe(String nom,int nb_faces,int BORNE){
        super(nom,nb_faces);
        this.BORNE=BORNE;
    }

    public int lancer(){
        int a=super.lancer();
        while(a<BORNE){
            a=super.lancer();
        }
        return a;
    }

    public String toString(){
        return super.toString()+" BORNE = "+this.BORNE;
    }
}
