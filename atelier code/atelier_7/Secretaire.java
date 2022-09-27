package atelier_7;
import java.util.LinkedList;
import java.util.GregorianCalendar;

public class Secretaire extends Employe{
    private LinkedList<Manager> listeManager;
    

    private Secretaire(String nom,String prenom,GregorianCalendar ddn,Adresse add,double salaire,GregorianCalendar dateEmbauche){
        super(nom,prenom,ddn,add,salaire,dateEmbauche);
        listeManager=new LinkedList<Manager>();
    }

    public static Secretaire createSecretaire(String nom,String prenom,GregorianCalendar ddn,Adresse add,double salaire,GregorianCalendar dateEmbauche){
        if(ageCorrect(ddn)){
            return new Secretaire(nom,prenom,ddn,add,salaire,dateEmbauche);
        }
        return null;
    }

    public void ajouterManager(Manager personne){
        if(listeManager.size()<5 && !(listeManager.contains(personne))){
            listeManager.add(personne);
            personne.ajouterSecretaire(this);
        }
    }

    public void supprimerManager(Manager manager){
        if(listeManager.contains(manager)){
            listeManager.remove(manager);
            if(manager.getSecretaire()!=null){
                manager.supprimerSecretaire(this);
            }
        }
    }

    public void affichListeManager(){
        System.out.println(listeManager);
    }

    public void augmenterLeSalaire(double pourcentage){
        super.augmenterLeSalaire((pourcentage+(0.1)*listeManager.size()));
    }

    public int getNbManager(){
        return listeManager.size();
    }
}
