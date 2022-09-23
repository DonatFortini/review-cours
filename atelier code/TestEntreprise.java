import atelier_7.Adresse;
import atelier_7.Personne;
import atelier_7.Employe;
import atelier_7.Secretaire;
import atelier_7.Manager;
import java.util.GregorianCalendar;

public class TestEntreprise {
    public static void main(String[] args) {
        
        GregorianCalendar greg=new GregorianCalendar(2010,7,20);
        Adresse add=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");

        GregorianCalendar greg1=new GregorianCalendar(2000,7,20);
        Adresse add1=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");

        GregorianCalendar greg2=new GregorianCalendar(1980,8,20);
        Adresse add2=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");
        
        Personne p0=new Personne("turlu", "tutu", greg, add);
        Personne p1=new Personne("turlu", "tutu", greg1, add1);
        Personne p2=new Personne("turlu", "toto", greg1, add1);
        Personne p3=new Personne("turlu", "tata", greg2, add2);
        Employe emp0=Employe.createEmploye(p0);
        Employe emp1=Employe.createEmploye(p1);

        System.out.println(emp0);
        System.out.println(emp1);

        Secretaire secretaire=Secretaire.createSecretaire(p2);
        Manager manager=Manager.createManager(p3);

        System.out.println(secretaire);
        System.out.println(manager);

        Manager.ajouterSecretaire(manager, secretaire);
        secretaire.affichListeManager();

        Manager.supprimerSecretaire(manager, secretaire);
        secretaire.affichListeManager();

        Manager.ajouterSecretaire(manager, secretaire);

        secretaire.augmenterLeSalaire(10);
        manager.augmenterLeSalaire(10);
        emp1.augmenterLeSalaire(10);

        System.out.println(secretaire);
        System.out.println(manager);
        System.out.println(emp1);
    }
}
