package atelier_7;
import java.util.LinkedList;
import java.util.GregorianCalendar;

public class Manager extends Employe{
    private LinkedList<Secretaire> secretaires;
    private static GregorianCalendar dateDuJour=new GregorianCalendar();

    private Manager(String nom,String prenom,GregorianCalendar ddn,Adresse add,double salaire,GregorianCalendar dateEmbauche){
        super(nom,prenom,ddn,add,salaire,dateEmbauche);
        secretaires=new LinkedList<Secretaire>();
    }

    public static Manager createManager(Personne personne){
        if(Personne.quelAge(personne)>16 && Personne.quelAge(personne)<65){
            return new Manager(personne.getNom(),personne.getPrenom(),personne.getDateNaissance(),personne.getAdresse(),1200.0,dateDuJour);
        }
        return null;
    }

    public void augmenterLeSalaire(double pourcentage){
        super.augmenterLeSalaire((pourcentage+(0.5)*this.calculAnnuite()));
    }

    public static void ajouterSecretaire(Manager p1 ,Secretaire p2){
        if(p1.secretaires.isEmpty() && Secretaire.getNbManager(p2)<5){
            p1.secretaires.add(p2);
            p2.ajouterManager(p1);
        }
    }

    public static void supprimerSecretaire(Manager p1 ,Secretaire p2){
        if(p1.secretaires.contains(p2)){
            p1.secretaires.remove(p2);
            p2.supprimerManager(p1);
        }
    }
}
