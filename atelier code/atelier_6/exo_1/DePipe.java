package atelier_6.exo_1;

public class DePipe extends De{
    private final int borne ;

    public DePipe(String nom,int nb_faces,int borne){
        super(nom,nb_faces);
        this.borne=borne;
    }

    public int lancer(){
        int a=super.lancer();
        while(a<borne){
            a=super.lancer();
        }
        return a;
    }

    public String toString(){
        return super.toString()+" borne = "+this.borne;
    }
}
