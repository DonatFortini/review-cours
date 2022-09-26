package atelier_7;

import java.util.GregorianCalendar;

public class Employe  extends Personne{
    private double salaire;
    private static final int AGE_MIN=16;
    private static final int AGE_MAX=65;
    private final GregorianCalendar DATE_EMBAUCHE;
    private static GregorianCalendar dateDuJour=new GregorianCalendar();

    protected Employe(String nom,String prenom,GregorianCalendar ddn,Adresse add,double salaire,GregorianCalendar dateEmbauche){
        super(nom, prenom, ddn, add);
        this.salaire=salaire;
        this.DATE_EMBAUCHE=dateEmbauche;
    }

    public static Employe createEmploye(String nom,String prenom,GregorianCalendar ddn,Adresse add,double salaire,GregorianCalendar dateEmbauche){
        if(ageCorrect(ddn)){
            return new Employe(nom,prenom,ddn,add,salaire,dateEmbauche);
        }
        return null;
    }

    public void augmenterLeSalaire(double pourcentage){
        if(pourcentage<0){
            System.err.println("le pourcentage doit etre positif");
        }
        else{
            salaire=salaire+(salaire*pourcentage)/100;
        }
    }

    public int calculAnnuite(){
        int depart =DATE_EMBAUCHE.get(DATE_EMBAUCHE.YEAR);
		int arrive= dateDuJour.get(dateDuJour.YEAR);
        return arrive-depart;
    }

    public String toString(){
        return super.toString()+"\n salaire:"+salaire;
    }

    public static boolean ageCorrect(GregorianCalendar ddn){
        return quelAge(ddn)>AGE_MIN && quelAge(ddn)<AGE_MAX;
    }

}
