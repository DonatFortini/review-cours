package atelier_7;
import java.util.LinkedList;
import java.util.GregorianCalendar;

public class Manager extends Employe{
    private Secretaire maSecretaire=null;
    

    private Manager(String nom,String prenom,GregorianCalendar ddn,Adresse add,double salaire,GregorianCalendar dateEmbauche){
        super(nom,prenom,ddn,add,salaire,dateEmbauche);
    }

    public static Manager createManager(String nom,String prenom,GregorianCalendar ddn,Adresse add,double salaire,GregorianCalendar dateEmbauche){
        if(ageCorrect(ddn)){
            return new Manager(nom,prenom,ddn,add,salaire,dateEmbauche);
        }
        return null;
    }

    public void augmenterLeSalaire(double pourcentage){
        super.augmenterLeSalaire((pourcentage+(0.5)*this.calculAnnuite()));
    }

    public void ajouterSecretaire(Secretaire secretaire){
        if(maSecretaire==null && secretaire.getNbManager()<5){
            maSecretaire=secretaire;
            secretaire.ajouterManager(this);
        }
    }

    public void supprimerSecretaire(Secretaire secretaire){
        if(maSecretaire.equals(secretaire)){
            maSecretaire=null;
            secretaire.supprimerManager(this);
        }
    }

    public Secretaire getSecretaire(){
        return maSecretaire;
    }
}
