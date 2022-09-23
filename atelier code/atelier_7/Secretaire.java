package atelier_7;
import java.util.LinkedList;
import java.util.GregorianCalendar;

public class Secretaire extends Employe{
    private LinkedList<Manager> listeManager;
    private static GregorianCalendar dateDuJour=new GregorianCalendar();

    private Secretaire(String nom,String prenom,GregorianCalendar ddn,Adresse add,double salaire,GregorianCalendar dateEmbauche){
        super(nom,prenom,ddn,add,salaire,dateEmbauche);
        listeManager=new LinkedList<Manager>();
    }

    public static Secretaire createSecretaire(Personne personne){
        if(Personne.quelAge(personne)>16 && Personne.quelAge(personne)<65){
            return new Secretaire(personne.getNom(),personne.getPrenom(),personne.getDateNaissance(),personne.getAdresse(),1200.0,dateDuJour);
        }
        return null;
    }

    public void ajouterManager(Manager personne){
        if(listeManager.size()<5){
            listeManager.add(personne);
        }
    }

    public void supprimerManager(Manager personne){
        if(listeManager.contains(personne)){
            listeManager.remove(personne);
        }
    }

    public void affichListeManager(){
        System.out.println(listeManager);
    }

    public void augmenterLeSalaire(double pourcentage){
        super.augmenterLeSalaire((pourcentage+(0.1)*listeManager.size()));
    }

    public static int getNbManager(Secretaire personne){
        return personne.listeManager.size();
    }
}
